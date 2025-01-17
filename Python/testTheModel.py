import librosa
import numpy as np
import tensorflow as tf

# Function to preprocess a single audio file
def preprocess_sound_file(file_path, sr=16000, n_mfcc=30, max_pad_len=100):
    """
    Preprocesses a single audio file to extract MFCC features.
    :param file_path: Path to the audio file
    :param sr: Sampling rate
    :param n_mfcc: Number of MFCC coefficients
    :param max_pad_len: Maximum padding length
    :return: Preprocessed MFCC input
    """
    try:
        # Load the audio file
        audio, _ = librosa.load(file_path, sr=sr)
        n_fft = min(1024, len(audio))  # Match the FFT window size used during training
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=n_fft // 2)

        # Pad or truncate to match the input size
        pad_width = max_pad_len - mfcc.shape[1]
        if pad_width > 0:
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
        else:
            mfcc = mfcc[:, :max_pad_len]

        return mfcc[..., np.newaxis]  # Add channel dimension for Conv2D
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

# Function to scale and quantize MFCC input
def quantize_input(mfcc_input, input_details):
    """
    Scales and quantizes the MFCC input to int8 based on model input requirements.
    :param mfcc_input: Preprocessed MFCC input
    :param input_details: Model input details from the TFLite interpreter
    :return: Quantized MFCC input
    """
    input_scale, input_zero_point = input_details[0]['quantization']
    if input_scale == 0:
        raise ValueError("Input quantization scale is zero, which is invalid.")
    
    # Scale and quantize
    quantized_input = ((mfcc_input / input_scale) + input_zero_point).astype(np.int8)
    return quantized_input

# Function to load the TFLite model
def load_tflite_model(tflite_model_path):
    """
    Loads the TFLite model and returns an interpreter.
    :param tflite_model_path: Path to the TFLite model file
    :return: TFLite Interpreter
    """
    interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
    interpreter.allocate_tensors()
    return interpreter

# Function to predict gunshot from a preprocessed input
def predict_gunshot(interpreter, mfcc_input):
    """
    Runs inference on a preprocessed MFCC input using the TFLite model.
    :param interpreter: TFLite Interpreter
    :param mfcc_input: Preprocessed MFCC input
    :return: Prediction score (float)
    """
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Quantize the MFCC input
    quantized_input = quantize_input(mfcc_input, input_details)

    # Ensure input shape matches model's requirements
    quantized_input = np.expand_dims(quantized_input, axis=0)  # Add batch dimension
    interpreter.set_tensor(input_details[0]['index'], quantized_input)
    interpreter.invoke()

    # Get the prediction
    output_data = interpreter.get_tensor(output_details[0]['index'])
    output_scale, output_zero_point = output_details[0]['quantization']

    # Dequantize the output
    prediction_score = output_scale * (output_data[0][0] - output_zero_point)
    return prediction_score

# Main workflow
if __name__ == "__main__":
    # Path to the new sound file and TFLite model
    new_audio_file = "audioFiles/gunshot.wav"  # Replace with your file path
    tflite_model_path = "fully_quantized_gunshot_model_v5.tflite"  # Replace with your model path

    print("Processing audio file...")
    # Step 1: Preprocess the sound file
    mfcc_input = preprocess_sound_file(new_audio_file)

    if mfcc_input is not None:
        print("Loading TFLite model...")
        # Step 2: Load the TFLite model
        interpreter = load_tflite_model(tflite_model_path)

        print("Running inference...")
        # Step 3: Run inference
        prediction_score = predict_gunshot(interpreter, mfcc_input)

        # Step 4: Interpret the result
        if prediction_score > 0.5:
            print(f"Prediction: Gunshot detected with confidence {prediction_score:.2f}")
        else:
            print(f"Prediction: No gunshot detected with confidence {1 - prediction_score:.2f}")
    else:
        print("Error: Unable to preprocess the audio file.")

