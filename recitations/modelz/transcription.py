import os
from pathlib import Path

from google.cloud import speech
import io
import json

BASE_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(__file__)))).parent

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{BASE_DIR}/core/credentials.json"


def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    with io.open(audio_file, "rb") as audio:
        content = audio.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ar-SA"
    )

    response = client.recognize(config=config, audio=audio)

    return response.results[0].alternatives[0].transcript if response.results else ""


def transcribe_dataset(annotation_file):
    with open(annotation_file, 'r', encoding='utf-8') as f:
        annotations = json.load(f)

    for annotation in annotations:
        audio_file = annotation['file_name']
        transcription = transcribe_audio(audio_file)
        annotation['transcription'] = transcription

    with open('transcribed_annotations.json', 'w', encoding='utf-8') as f:
        json.dump(annotations, f, ensure_ascii=False, indent=4)


annotation_file = f"{BASE_DIR}/datasets/annotations/annotations.json"
transcribe_dataset(annotation_file)
