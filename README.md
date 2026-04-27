# 🎬➡️📄 YouTube Video to Insightful Article & PDF

An end-to-end AI-powered pipeline that transforms any YouTube video into a structured, ready-to-publish article with a downloadable PDF — automatically.

> Built as part of my internship project at **[Innomatics Research Labs](https://www.innomatics.in/)**

---

## ✨ Features

- 🔗 Paste any YouTube URL (including Shorts)
- 🎧 Automatically downloads and extracts audio
- 📝 Transcribes speech using OpenAI Whisper
- 🤖 Converts transcript into a clean, insightful article using Claude AI
- 📄 Generates a professionally formatted downloadable PDF
- 🖥️ Simple, intuitive Streamlit web interface

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| yt-dlp | YouTube audio download |
| FFmpeg | Audio processing |
| OpenAI Whisper | Speech-to-text transcription |
| Claude API (Anthropic) | Article generation |
| Streamlit | Web interface |
| ReportLab / FPDF | PDF generation |

---

## 📁 Project Structure

```
YT_TO_ARTICLE/
├── app.py                  # Streamlit entry point
├── main.py                 # Pipeline orchestrator
├── config.py               # API keys and settings
├── requirements.txt        # Python dependencies
├── cookies.txt             # YouTube cookies (not committed)
├── modules/
│   ├── downloader.py       # YouTube audio downloader
│   ├── transcriber.py      # Whisper transcription
│   ├── cleaner.py          # Transcript cleaning
│   ├── llm_processor.py    # Claude AI article generation
│   └── pdf_generator.py    # PDF creation
└── outputs/
    ├── audio/              # Downloaded audio files
    └── pdf/                # Generated PDFs
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/yt-to-article.git
cd yt-to-article
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and update the `ffmpeg_location` path in `modules/downloader.py`.

### 5. Set up API keys

Create a `config.py` file (or set environment variables):

```python
ANTHROPIC_API_KEY = "your_claude_api_key_here"
```

### 6. Add YouTube cookies (optional but recommended)

Export `cookies.txt` from your browser using the **"Get cookies.txt LOCALLY"** Chrome extension while logged into YouTube. Place it in the project root.

### 7. Run the app

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your Claude API key from [console.anthropic.com](https://console.anthropic.com) |

---

## 📝 How It Works

```
YouTube URL
    │
    ▼
[downloader.py]  →  Downloads audio using yt-dlp
    │
    ▼
[transcriber.py] →  Transcribes audio using Whisper
    │
    ▼
[cleaner.py]     →  Cleans and formats the transcript
    │
    ▼
[llm_processor.py] → Generates article using Claude AI
    │
    ▼
[pdf_generator.py] → Creates downloadable PDF
```

---

## ⚠️ Important Notes

- `cookies.txt` is excluded from this repo (see `.gitignore`) — never commit your cookies
- `config.py` with API keys is also excluded — never commit API keys
- The `outputs/` folder is excluded — generated files stay local
- Make sure FFmpeg is installed and the path is correctly set in `downloader.py`

---

## 🙏 Acknowledgements

- **[Innomatics Research Labs](https://www.innomatics.in/)** — for the internship opportunity and project guidance
- [OpenAI Whisper](https://github.com/openai/whisper) — open-source transcription model
- [Anthropic Claude](https://www.anthropic.com/) — AI article generation
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube downloader
