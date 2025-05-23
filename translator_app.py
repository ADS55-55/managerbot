import streamlit as st
from googletrans import Translator
import csv
from datetime import datetime

translator = Translator()

language_map = {
    "🇮🇳 Hindi": "hi",
    "🇮🇳 Tamil": "ta",
    "🇪🇸 Spanish": "es",
    "🇫🇷 French": "fr",
    "🇮🇹 Italian": "it"
}

st.set_page_config(page_title="ManagerBot Translator", page_icon="🌐")
st.title("🌍 Multi-Language Translator (ManagerBot)")
st.write("Type a word or sentence and translate it into multiple languages.")

text_to_translate = st.text_input("Enter a word or sentence:")
selected_languages = st.multiselect("Choose languages", list(language_map.keys()), default=list(language_map.keys()))

if st.button("Translate"):
    if text_to_translate:
        st.subheader("Translations:")
        with open("translation_history.csv", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            for lang in selected_languages:
                try:
                    result = translator.translate(text_to_translate, dest=language_map[lang])
                    st.write(f"**{lang}:** {result.text}")
                    writer.writerow([datetime.now(), text_to_translate, lang, result.text])
                except Exception as e:
                    st.write(f"{lang}: ❌ Error - {e}")
                    writer.writerow([datetime.now(), text_to_translate, lang, f"Error - {e}"])
    else:
        st.warning("Please enter some text to translate.")
