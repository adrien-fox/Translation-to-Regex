import streamlit as st
from deep_translator import GoogleTranslator
from unidecode import unidecode
import pandas as pd


st.set_page_config(page_title = "Translation to Regex",
                   page_icon = ":fox:",
                   layout = 'wide')

st.header("Translation 2 Regex")

col1, colu2 = st.columns(2)

with col1:
    word_1_FR = st.text_input("🇫🇷 FR First Word 🇫🇷", value = "chocolat")

    word_1_EN = unidecode(GoogleTranslator(source = "fr", target = "en").translate(word_1_FR))
    word_1_ES = unidecode(GoogleTranslator(source = "fr", target = "es").translate(word_1_FR))
    word_1_IT = unidecode(GoogleTranslator(source = "fr", target = "it").translate(word_1_FR))
    word_1_DE = unidecode(GoogleTranslator(source = "fr", target = "de").translate(word_1_FR))
    word_1_NL = unidecode(GoogleTranslator(source = "fr", target = "nl").translate(word_1_FR))

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write("🇬🇧 EN 🇬🇧")
        st.code(str(word_1_EN).lower())
    with col2:
        st.write("🇪🇸 ES 🇪🇸")
        st.code(str(word_1_ES).lower())
    with col3:
        st.write("🇮🇹 IT 🇮🇹")
        st.code(str(word_1_IT).lower())
    with col4:
        st.write("🇩🇪 DE 🇩🇪")
        st.code(str(word_1_DE).lower())
    with col5:
        st.write("🇳🇱 NL 🇳🇱")
        st.code(str(word_1_NL).lower())

    liste_1 = [word_1_FR.lower(), word_1_EN.lower(), word_1_ES.lower(), word_1_IT.lower(), word_1_DE.lower(), word_1_NL.lower()]

    unique_liste_1 = list(set(liste_1))

    st.write("Unique translation")
    st.code(unique_liste_1)
    st.write("Regex")
    st.code("(" + "|".join(unique_liste_1) + ")")




with colu2:
    word_2_FR = st.text_input("🇫🇷 FR Second Word 🇫🇷", value = "yaourt")
    word_2_EN = GoogleTranslator(source = "fr", target = "en").translate(word_2_FR)
    word_2_ES = GoogleTranslator(source = "fr", target = "es").translate(word_2_FR)
    word_2_IT = GoogleTranslator(source = "fr", target = "it").translate(word_2_FR)
    word_2_DE = GoogleTranslator(source = "fr", target = "de").translate(word_2_FR)
    word_2_NL = GoogleTranslator(source = "fr", target = "nl").translate(word_2_FR)

    colu1, colu2, colu3, colu4, colu5 = st.columns(5)

    with colu1:
        st.write("🇬🇧 EN 🇬🇧")
        st.code(str(word_2_EN).lower())
    with colu2:
        st.write("🇪🇸 ES 🇪🇸")
        st.code(str(word_2_ES).lower())
    with colu3:
        st.write("🇮🇹 IT 🇮🇹")
        st.code(str(word_2_IT).lower())
    with colu4:
        st.write("🇩🇪 DE 🇩🇪")
        st.code(str(word_2_DE).lower())
    with colu5:
        st.write("🇳🇱 NL 🇳🇱")
        st.code(str(word_2_NL).lower())

    liste_2 = [word_2_FR.lower(), word_2_EN.lower(), word_2_ES.lower(), word_2_IT.lower(), word_2_DE.lower(), word_2_NL.lower()]

    unique_liste_2 = list(set(liste_2))

    st.write("Unique translation")
    st.code(unique_liste_2)
    st.write("Regex")
    st.code("(" + "|".join(unique_liste_2) + ")")

st.write("Final Combination Regex")
st.code("(" + "|".join(unique_liste_1) + ").*(" + "|".join(unique_liste_2) + ")|(" + "|".join(unique_liste_2) + ").*(" + "|".join(unique_liste_1) + ")")


