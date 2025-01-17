import os
import librosa
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Function to load and preprocess the UrbanSound8K dataset
def load_urbansound_data(metadata_path, audio_dir, sr=16000, n_mfcc=30, max_pad_len=100):
    """
    Load and preprocess the dataset.
    :param metadata_path: Path to the metadata CSV
    :param audio_dir: Path to audio directory
    :param sr: Sampling rate
    :param n_mfcc: Number of MFCC coefficients
    :param max_pad_len: Fixed length for padding/truncation
    :return: Preprocessed dataset (X, y)
    """
    metadata = pd.read_csv(metadata_path)
    X, y = [], []
    for index, row in metadata.iterrows():
        file_path = os.path.join(audio_dir, f"fold{row['fold']}", row['slice_file_name'])
        try:
            # Load audio and extract MFCCs
            audio, _ = librosa.load(file_path, sr=sr)
            n_fft = min(1024, len(audio))  # Slightly larger FFT window
            mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=n_fft // 2)
            
            # Pad or truncate MFCCs
            pad_width = max_pad_len - mfcc.shape[1]
            if pad_width > 0:
                mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
            else:
                mfcc = mfcc[:, :max_pad_len]
            X.append(mfcc)
            
            # Assign label (1 for gunshot, 0 otherwise)
            y.append(1 if row['class'] == 'gun_shot' else 0)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    return np.array(X), np.array(y)

# Paths to metadata and audio files
metadata_path = 'urbansound8k/metadata/UrbanSound8K.csv'
audio_dir = 'urbansound8k/audio'

print("Loading dataset...")
X, y = load_urbansound_data(metadata_path, audio_dir)
X = X[..., np.newaxis]  # Add channel dimension for Conv2D
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def create_tflite_compatible_model(input_shape):
    """
    Create a TFLite-compatible model with increased accuracy.
    :param input_shape: Shape of the input data
    :return: Compiled Keras model
    """
    model = tf.keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(16, (3, 3), activation='relu', padding='same'),  # Larger filters
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        layers.GlobalAveragePooling2D(),
        layers.Dense(32, activation='relu'),  # Increased neurons
        layers.Dense(1, activation='sigmoid')  # Binary classification
    ])
    return model

# Initialize and compile the model
print("Creating model...")
model = create_tflite_compatible_model(X_train.shape[1:])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
print("Training model...")
history = model.fit(X_train, y_train, validation_split=0.2, epochs=20, batch_size=16)

# Evaluate the model
print("Evaluating model...")
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_accuracy}")

# Visualize training performance
def plot_training_history(history):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.legend()
    plt.title('Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.legend()
    plt.title('Loss')
    plt.show()

plot_training_history(history)

# Generate confusion matrix
def plot_confusion_matrix(y_true, y_pred, labels):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap='Blues', values_format='d')
    plt.title("Confusion Matrix")
    plt.show()

# Predict and visualize confusion matrix
y_pred = (model.predict(X_test) > 0.5).astype("int32")
plot_confusion_matrix(y_test, y_pred, labels=['Non-Gunshot', 'Gunshot'])

# Convert to a fully quantized TFLite model
print("Converting model to fully quantized TFLite...")
def representative_data_gen():
    for i in range(100):
        # Use actual preprocessed data samples
        yield [X_train[i:i+1].astype(np.float32)]


converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_data_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8  # Ensure inputs are quantized
converter.inference_output_type = tf.int8 # Ensure outputs are quantized
quantized_tflite_model = converter.convert()

# Save the TFLite model
quantized_tflite_model_path = 'fully_quantized_gunshot_model_v5.tflite'
with open(quantized_tflite_model_path, 'wb') as f:
    f.write(quantized_tflite_model)
print(f"Fully Quantized TFLite model saved to {quantized_tflite_model_path}")

print("Model training, evaluation, and conversion completed.")

