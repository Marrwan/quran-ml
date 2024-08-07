import os
import json
from pathlib import Path

from django.conf import settings


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
BASE_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(__file__))))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{BASE_DIR}/core/credentials.json"


def annotate_dataset(audio_dir):
    annotations = []

    for file_name in os.listdir(audio_dir):
        if file_name.endswith('.mp3'):
            surah_number = file_name.split('.')[0]
            audio_file = os.path.join(audio_dir, file_name)
            json_file = os.path.join(audio_dir, f'{surah_number}.json')

            with open(json_file, 'r', encoding='utf-8') as f:
                transcription_data = json.load(f)

            for ayah, data in transcription_data.items():
                annotation = {
                    'file_name': audio_file,
                    'surah': surah_number,
                    'ayah': ayah,
                    'transcription': data['text']
                }
                annotations.append(annotation)

    with open('datasets/annotations/annotations.json', 'w', encoding='utf-8') as f:
        json.dump(annotations, f, ensure_ascii=False, indent=4)

audio_dir = f"{BASE_DIR}/datasets"
# audio_dir = settings.DATASETS
print("AUDO DIR", audio_dir)
annotate_dataset(audio_dir)
