import streamlit as st
from deep_translator import GoogleTranslator
import pandas as pd

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(page_title="ManagerBot Translator", page_icon="🌍")

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    h1 {
        color: #4CAF50;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput > div > div > input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- TITLE ----------------------
st.markdown("<h1 style='text-align: center;'>🌍 ManagerBot Translator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Translate text into multiple languages instantly!</p><hr>", unsafe_allow_html=True)

# ---------------------- SIDEBAR INPUTS ----------------------
st.sidebar.title("🌐 Translation Settings")

language_map = {
    "🇮🇳 Hindi": "hi",
    "🇮🇳 Tamil": "ta",
    "🇪🇸 Spanish": "es",
    "🇫🇷 French": "fr",
    "🇮🇹 Italian": "it"
}

text_to_translate = st.sidebar.text_input("Enter a word or sentence:")
selected_languages = st.sidebar.multiselect("Choose languages", list(language_map.keys()), default=list(language_map.keys()))

# ---------------------- TRANSLATION LOGIC ----------------------
if 'history' not in st.session_state:
    st.session_state.history = []

if st.sidebar.button("Translate"):
    if text_to_translate:
        st.subheader("📝 Translations:")
        for lang in selected_languages:
            try:
                translated = GoogleTranslator(source='auto', target=language_map[lang]).translate(text_to_translate)
                st.write(f"**{lang}:** {translated}")
                st.session_state.history.append([text_to_translate, lang, translated])
            except Exception as e:
                st.write(f"{lang}: ❌ Error - {e}")
    else:
        st.warning("Please enter some text to translate.")

# ---------------------- DOWNLOAD TRANSLATION HISTORY ----------------------
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history, columns=["Original Text", "Language", "Translation"])
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download All Translations", data=csv, file_name="translations.csv", mime="text/csv")
