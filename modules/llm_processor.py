from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

# 🔹 Split text into chunks (IMPORTANT)
def split_text(text, max_words=400):
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


# 🔹 Generate article with chunking (MAP-REDUCE)
def generate_article(transcript):

    chunks = split_text(transcript)

    partial_summaries = []

    # STEP 1: Summarize each chunk
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")

        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": f"""
The following is part of a transcript (may contain errors).

Task:
- Understand the content
- Clean mistakes
- Summarize clearly

Text:
{chunk}
"""
                }
            ]
        )

        partial_summaries.append(response.choices[0].message.content)

    # STEP 2: Combine summaries
    combined_text = " ".join(partial_summaries)

    # STEP 3: Final article generation
    final_response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""
Create a well-structured article from this content.

Include:
- Title
- Introduction
- Step-by-step explanation (if tutorial)
- Key insights
- Conclusion

Content:
{combined_text}
"""
            }
        ]
    )

    return final_response.choices[0].message.content