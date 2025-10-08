import streamlit as st
from groq import Groq, APIStatusError  
import os
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="📝 Document Summarizer (Groq)")

st.title("📝 Document Summarizer Using LLM")
st.write("Summarize any text using Groq’s API. Choose from different summarization styles.")

input_method = st.radio("Input Method:", ("Paste Text", "Upload File"))

user_text = ""

if input_method == "Paste Text":
    user_text = st.text_area("Enter your text below:", height=300)
elif input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file:
        try:
            user_text = uploaded_file.read().decode("utf-8")
        except Exception as e:
            st.error("Error reading file: " + str(e))

style = st.selectbox("Select Summarization Style", ["Brief", "Detailed", "Bullet Points"])
style_map = {
    "Brief": "Summarize this text briefly:",
    "Detailed": "Write a detailed summary of the following text:",
    "Bullet Points": "Summarize the text into concise bullet points:"
}

if st.button("Generate Summary"):
    if not user_text.strip():
        st.warning("Please provide some text input first.")
    else:
        with st.spinner("Generating summary..."):
            prompt = f"{style_map[style]}\n\n{user_text}"
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",  
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                summary = response.choices[0].message.content.strip()
                st.success("✅ Summary generated successfully:")
                st.text_area("Summary", value=summary, height=300)
            except APIStatusError as e:
                st.error(f"Groq API status error {e.status_code}: {e.response}")
            except Exception as e:
                st.error(f"Error from Groq API: {str(e)}")
