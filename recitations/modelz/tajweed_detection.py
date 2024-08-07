def detect_errors(transcript):
    errors = []
    if "incorrect_word" in transcript:
        errors.append({"error": "Incorrect pronunciation", "word": "incorrect_word"})
    return errors
