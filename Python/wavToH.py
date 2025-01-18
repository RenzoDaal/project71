import numpy as np
import librosa

def wav_to_h_with_pcm(wav_file_path, h_file_path, array_name="audio_data", save_pcm="audio_data.npy"):
    """
    Converts a .wav file into a .h file with resampled mono PCM data.
    Also saves the PCM data as .npy for validation.
    :param wav_file_path: Path to the .wav file
    :param h_file_path: Path to save the .h file
    :param array_name: Name of the array in the .h file
    :param save_pcm: Path to save the PCM data for validation
    """
    try:
        # Load the .wav file and resample it to 16,000 Hz mono
        print(f"Loading {wav_file_path}...")
        audio, sr = librosa.load(wav_file_path, sr=16000, mono=True)  # Force mono and resample to 16kHz
        print(f"Resampled audio to 16kHz mono. Original sample rate: {sr} Hz, Frames: {len(audio)}")

        # Convert audio to 16-bit PCM format
        audio_pcm = np.round(audio * 32768).astype(np.int16)

        # Save the PCM data for validation
        np.save(save_pcm, audio_pcm)
        print(f"PCM data saved to {save_pcm}")

        # Save as a .h file
        with open(h_file_path, 'w') as h_file:
            h_file.write(f"// Converted from {wav_file_path}\n")
            h_file.write(f"// Mono, Sample Rate: 16000, Frames: {len(audio_pcm)}\n")
            h_file.write(f"const int16_t {array_name}[] = {{\n")
            h_file.write(", ".join(map(str, audio_pcm)))
            h_file.write("\n};\n")
        print(f"Successfully converted {wav_file_path} to {h_file_path}")
    except Exception as e:
        print(f"Error converting {wav_file_path} to .h: {e}")

# Example usage
if __name__ == "__main__":
    wav_file = "audioFiles/gunshot.wav"  # Path to your .wav file
    h_file = "audio_data_gunshot_resampled.h"  # Path to save the .h file
    pcm_file = "audio_data_gunshot.npy"  # Path to save the PCM data

    print("Converting .wav to .h file with resampled mono PCM data...")
    wav_to_h_with_pcm(wav_file, h_file, array_name="audio_data_resampled", save_pcm=pcm_file)


