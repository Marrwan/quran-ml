import os
from pathlib import Path

from google.cloud import speech

BASE_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(__file__)))).parent

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{BASE_DIR}/core/credentials.json"

audio = f"{BASE_DIR}/datasets/001.wav"


def transcribe_audio(audio_file):
    client = speech.SpeechClient()
    # Load the audio file into memory
    with open(audio_file, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ar-SA"
    )
    response = client.recognize(config=config, audio=audio)
    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript
    return transcript


# os.path("")
print(transcribe_audio(audio))
