import os
from pathlib import Path
import numpy as np
import librosa
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from joblib import dump

BASE_DIR = Path(os.path.join(os.path.dirname(os.path.dirname(__file__)))).parent
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{BASE_DIR}/core/credentials.json"


def extract_features(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccs_scaled = np.mean(mfccs.T, axis=0)
        return mfccs_scaled
    except Exception as e:
        print(f"Error encountered while parsing file: {file_name}")
        print(e)
        return None


def load_data(audio_dir):
    features = []
    labels = []

    for file_name in os.listdir(audio_dir):
        if file_name.endswith('.wav'):
            surah_number = file_name.split('.')[0]
            audio_file = os.path.join(audio_dir, file_name)
            data = extract_features(audio_file)
            if data is not None:
                features.append(data)
                labels.append(surah_number)

    return np.array(features), np.array(labels)


audio_dir = f"{BASE_DIR}/datasets/wav"
# features, labels = load_data(audio_dir)

# Debugging: Print the unique labels and their counts
# unique_labels, counts = np.unique(labels, return_counts=True)
# print("Unique labels and their counts:", dict(zip(unique_labels, counts)))

# # Check if there are more than one class
# if len(unique_labels) <= 1:
#     raise ValueError("The dataset must contain at least two classes.")

# Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train an SVM model
# model = SVC(kernel='linear')
# model.fit(X_train, y_train)
#
# # Evaluate the model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy * 100:.2f}%')
#
# # Save the trained model
# dump(model, 'surah_detection_model.joblib')
# print("Features:", features)
# print("Labels:", labels)

from joblib import load

# Load the trained model
model = load('surah_detection_model.joblib')


def predict_surah(audio_file):
    features = extract_features(audio_file)
    if features is not None:
        features = features.reshape(1, -1)  # Reshape for single sample prediction
        prediction = model.predict(features)
        return prediction[0]
    return None


# Example usage
audio_file = f"{BASE_DIR}/datasets/nas.wav"
predicted_surah = predict_surah(audio_file)
print(f'Predicted Surah: {predicted_surah}')
