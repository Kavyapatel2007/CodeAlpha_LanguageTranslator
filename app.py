import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translator")
st.write("Translate text between multiple languages instantly.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Italian": "it",
    "Korean": "ko",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Turkish": "tr",
    "Greek": "el",
    "Thai": "th",
    "Vietnamese": "vi",
    "Bengali": "bn",
    "Urdu": "ur",
    "Punjabi": "pa"
}

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text.strip():

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed!")
        st.write("### Translated Text")

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )

    else:
        st.warning("Please enter some text.")