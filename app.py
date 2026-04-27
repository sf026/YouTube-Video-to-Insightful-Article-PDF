import streamlit as st
from main import run_pipeline

st.set_page_config(page_title="YouTube → Article Generator")

st.title("🎥 YouTube to Article & PDF")

url = st.text_input("Enter YouTube URL")

if st.button("Generate"):
    if url:
        with st.spinner("Processing..."):
            result = run_pipeline(url)

        st.subheader("📄 Transcript")
        st.write(result["transcript"])

        st.subheader("🧠 Article")
        st.write(result["article"])

        with open(result["pdf"], "rb") as f:
            st.download_button(
                "📥 Download PDF",
                f,
                file_name="article.pdf"
            )
    else:
        st.warning("Please enter a URL")