from modules.downloader import download_audio
from modules.transcriber import transcribe_audio
from modules.cleaner import clean_text
from modules.llm_processor import generate_article
from modules.pdf_generator import generate_pdf

def run_pipeline(url):
    print("Downloading audio...")
    audio_path = download_audio(url)

    print("Transcribing...")
    transcript = transcribe_audio(audio_path)

    print("Cleaning...")
    clean_transcript = clean_text(transcript)

    print("Generating article...")
    article = generate_article(clean_transcript)

    print("Generating PDF...")
    pdf_path = generate_pdf(article)

    return {
        "transcript": clean_transcript,
        "article": article,
        "pdf": pdf_path
    }


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    result = run_pipeline(url)

    print("\n--- ARTICLE ---\n")
    print(result["article"])