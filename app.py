import streamlit as st
from google import genai
from google.genai.errors import APIError
from streamlit.errors import StreamlitSecretNotFoundError

MODEL_NAME = "gemini-3.5-flash"

st.set_page_config(page_title="AI Document Assistant", page_icon="📄")
st.title("AI Document Understanding Assistant")
st.write("Upload a text document to summarize it or ask questions about it.")


def generate_response(prompt: str) -> str | None:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except (KeyError, StreamlitSecretNotFoundError):
        st.error(
            "Gemini is not configured. Add GEMINI_API_KEY to the app's "
            "Streamlit Secrets before using the AI features."
        )
        return None

    if not api_key:
        st.error("GEMINI_API_KEY is empty. Add a valid key in Streamlit Secrets.")
        return None

    client = genai.Client(api_key=api_key)
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
    except APIError as error:
        st.error(f"Gemini API request failed: {error}")
        return None
    finally:
        client.close()

    if not response.text:
        st.error("Gemini returned an empty response. Please try again.")
        return None

    return response.text


uploaded_file = st.file_uploader("Upload a text document", type=["txt"])

if uploaded_file is not None:
    try:
        document = uploaded_file.getvalue().decode("utf-8")
    except UnicodeDecodeError:
        st.error("The uploaded file is not valid UTF-8 text.")
        st.stop()

    if not document.strip():
        st.warning("The uploaded document is empty.")
        st.stop()

    st.success(f"Loaded {uploaded_file.name}")
    with st.expander("View document"):
        st.text(document)

    if st.button("Summarize document"):
        with st.spinner("Gemini is summarizing the document..."):
            summary = generate_response(
                "Provide a clear, brief, and structured summary of this document:\n\n"
                + document
            )
        if summary:
            st.subheader("Summary")
            st.write(summary)

    question = st.text_input("What would you like to know about the document?")
    if st.button("Ask a question"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            prompt = (
                "Answer the question using only the document below. "
                "If the answer is not present, say so.\n\n"
                f"Document:\n{document}\n\nQuestion: {question}"
            )
            with st.spinner("Gemini is finding the answer..."):
                answer = generate_response(prompt)
            if answer:
                st.subheader("Answer")
                st.write(answer)
