import streamlit as st
from deep_translator import GoogleTranslator

language_map = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Spanish": "es",
    "French": "fr",
    "Italian": "it"
}

st.set_page_config(page_title="ManagerBot Translator", page_icon="🌐")
st.title("🌍 Multi-Language Translator (ManagerBot)")
st.write("Type a word or sentence and translate it into multiple languages.")

text_to_translate = st.text_input("Enter a word or sentence:")
selected_languages = st.multiselect("Choose languages", list(language_map.keys()), default=list(language_map.keys()))

if st.button("Translate"):
    if text_to_translate:
        st.subheader("Translations:")
        for lang in selected_languages:
            try:
                translated = GoogleTranslator(source='auto', target=language_map[lang]).translate(text_to_translate)
                st.write(f"**{lang}:** {translated}")
            except Exception as e:
                st.write(f"{lang}: ❌ Error - {e}")
    else:
        st.warning("Please enter some text to translate.")
