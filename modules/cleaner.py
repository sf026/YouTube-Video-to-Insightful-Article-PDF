import re

def clean_text(text):
    # Remove repeated words
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)

    # Remove weird characters
    text = re.sub(r'[^a-zA-Z0-9.,!? ]', '', text)

    return " ".join(text.split())