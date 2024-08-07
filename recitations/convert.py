import os
from pydub import AudioSegment
from pathlib import Path

BASE_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(__file__)))).parent

# ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav

def convert_mp3_to_wav(input_dir, output_dir, sample_rate=16000):
    """
    Convert MP3 files to WAV format with a specified sample rate.

    Args:
        input_dir (str): Directory containing MP3 files.
        output_dir (str): Directory to save the converted WAV files.
        sample_rate (int): Desired sample rate for the output WAV files.
    """
    print("HERE")
    if not os.path.exists(output_dir):
        print("NODIR")
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        print(file_name)
        if file_name.endswith('.mp3'):
            mp3_path = os.path.join(input_dir, file_name)
            wav_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.wav')

            # Load the MP3 file
            audio = AudioSegment.from_mp3(mp3_path)
            # Set the sample rate
            audio = audio.set_frame_rate(sample_rate)
            # Export as WAV
            audio.export(wav_path, format='wav')

            print(f"Converted {mp3_path} to {wav_path}")


# Define your input and output directories
dir = f"{BASE_DIR}/datasets"
output_dir = f"{BASE_DIR}/datasets/wav"

convert_mp3_to_wav(dir, dir)
