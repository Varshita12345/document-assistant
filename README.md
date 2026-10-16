# AI Document Assistant

A Streamlit app for summarizing text documents and asking questions about them
with the Gemini API. The command-line `main.py` remains available for local
Ollama use.

## Run locally

1. Install the dependencies with `pip install -r requirements.txt`.
2. Create `.streamlit/secrets.toml` with:

   ```toml
   GEMINI_API_KEY = "your-Gemini-API-key"
   ```

3. Start the web app with `streamlit run app.py`.

Keep the API key private. `.streamlit/secrets.toml` is ignored by Git.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) with
   GitHub and choose **Create app**.
3. Select `Varshita12345/document-assistant`, the `main` branch, and `app.py`
   as the app file.
4. Before deploying, open **Advanced settings / Secrets** and add:

   ```toml
   GEMINI_API_KEY = "your-Gemini-API-key"
   ```

5. Deploy. Streamlit will display the public app URL when deployment succeeds.
