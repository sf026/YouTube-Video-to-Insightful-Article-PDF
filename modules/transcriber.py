from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel(
        "base",              # better than tiny
        compute_type="int8"  # fast on CPU
    )

    segments, _ = model.transcribe(
        audio_path,
        language="en"        # force English
    )

    transcript = ""
    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()