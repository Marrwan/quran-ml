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
audio_file = 'path_to_new_audio_file.wav'
predicted_surah = predict_surah(audio_file)
print(f'Predicted Surah: {predicted_surah}')
