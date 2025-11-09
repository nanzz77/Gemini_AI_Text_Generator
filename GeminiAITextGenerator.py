import streamlit as st
import google.generativeai as genai

# --- App Title and Configuration ---
st.set_page_config(
    page_title="Gemini AI Text Generation",
    page_icon="✨",
    layout="centered"
)

st.title("📝 Text Generation App")
st.caption("Powered by ----")

# --- API Key and Model Configuration ---
try:
    # Configure the Gemini API with the key from Streamlit secrets
    genai.configure(api_key="enter your api key here")
    # Create a Gemini model instance
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error(f"Error configuring the Gemini API: {e}")
    st.error("Please make sure your Gemini API key is correctly set up.")
    st.stop()


# --- Sidebar for App Description ---
with st.sidebar:
    st.header("About")
    st.markdown("""
    This application demonstrates the text generation capabilities of Google's Gemini AI.
    Enter a prompt in the text area and let Gemini generate a creative and relevant response.
    """)
    st.header("How to Use")
    st.markdown("""
    1.  Enter your desired text prompt in the input box on the main page.
    2.  Click the 'Generate Text' button.
    3.  The generated text from Gemini AI will appear below.
    """)

# --- Main Application Logic ---
prompt = st.text_area("Enter your prompt here:", height=150, placeholder="e.g., Write a short poem about a rainy day")

if st.button("Generate Text"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            try:
                # Generate content from the prompt
                response = model.generate_content(prompt)
                
                st.subheader("Generated Text:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred during text generation: {e}")
    else:
        st.warning("Please enter a prompt to generate text.")