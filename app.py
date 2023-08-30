import streamlit as st
from deep_translator import GoogleTranslator
from unidecode import unidecode
import pandas as pd
from streamlit_option_menu import option_menu


st.set_page_config(page_title = "Translation to Regex",
                   page_icon = ":fox:",
                   layout = 'wide')

with st.sidebar:

    navigation = option_menu("Navigation", ["Multiple Words Translator","2-Words Combination Translator"],
                            icons=['arrow-left-right', 'bookmark-check',],
                            menu_icon="app-indicator", default_index=0,
                            styles={
        "container": {"padding": "5!important", "background-color": "#0e1117"},
        "icon": {"color": "#774ee0", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if navigation == "2-Words Combination Translator" :

    st.header("2-Words Combination Translator")

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

        liste_1 = [unidecode(word_1_FR).lower(), word_1_EN.lower(), word_1_ES.lower(), word_1_IT.lower(), word_1_DE.lower(), word_1_NL.lower()]

        unique_liste_1 = list(set(liste_1))

        st.write("Unique translation")
        st.code(unique_liste_1)
        st.write("Regex")
        st.code("(" + "|".join(unique_liste_1) + ")")




    with colu2:
        word_2_FR = st.text_input("🇫🇷 FR Second Word 🇫🇷", value = "yaourt")
        word_2_EN = unidecode(GoogleTranslator(source = "fr", target = "en").translate(word_2_FR))
        word_2_ES = unidecode(GoogleTranslator(source = "fr", target = "es").translate(word_2_FR))
        word_2_IT = unidecode(GoogleTranslator(source = "fr", target = "it").translate(word_2_FR))
        word_2_DE = unidecode(GoogleTranslator(source = "fr", target = "de").translate(word_2_FR))
        word_2_NL = unidecode(GoogleTranslator(source = "fr", target = "nl").translate(word_2_FR))

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

        liste_2 = [unidecode(word_2_FR).lower(), word_2_EN.lower(), word_2_ES.lower(), word_2_IT.lower(), word_2_DE.lower(), word_2_NL.lower()]

        unique_liste_2 = list(set(liste_2))

        st.write("Unique translation")
        st.code(unique_liste_2)
        st.write("Regex")
        st.code("(" + "|".join(unique_liste_2) + ")")

    st.write("Final Combination Regex")
    st.code("(" + "|".join(unique_liste_1) + ").*(" + "|".join(unique_liste_2) + ")|(" + "|".join(unique_liste_2) + ").*(" + "|".join(unique_liste_1) + ")")

if navigation == "Multiple Words Translator":

    st.header("Multiple Words Translator")

    words_input = st.text_area("Enter a list of words you want to translate (please, enter it in the same format as below with ';' separator)", value = 'citron;\nfraise;\nananas',height = 150)

    words_input = ''.join(words_input.splitlines())

    words_input_list = list(words_input.split(";"))

    words_input_list_translated =[]

    if st.button("Translate and Create Regex") :

        colu1, colu2, colu3, colu4, colu5, colu6 = st.columns(6)

        with colu1 :
            st.markdown("🇫🇷 FR 🇫🇷")
        with colu2 : 
            st.markdown("🇬🇧 EN 🇬🇧")
        with colu3 : 
            st.markdown("🇩🇪 DE 🇩🇪")
        with colu4 : 
            st.markdown("🇪🇸 ES 🇪🇸")
        with colu5 : 
            st.markdown("🇮🇹 IT 🇮🇹")
        with colu6 : 
            st.markdown("🇳🇱 NL 🇳🇱")

        for words in words_input_list : 
            words_FR = unidecode(GoogleTranslator(source = "fr", target = "fr").translate(words)).lower()
            words_EN = unidecode(GoogleTranslator(source = "fr", target = "en").translate(words)).lower()
            words_DE = unidecode(GoogleTranslator(source = "fr", target = "de").translate(words)).lower()
            words_ES = unidecode(GoogleTranslator(source = "fr", target = "es").translate(words)).lower()
            words_IT = unidecode(GoogleTranslator(source = "fr", target = "it").translate(words)).lower()
            words_NL = unidecode(GoogleTranslator(source = "fr", target = "nl").translate(words)).lower()
            words_input_list_translated.append(words_FR)
            words_input_list_translated.append(words_EN)
            words_input_list_translated.append(words_DE)
            words_input_list_translated.append(words_ES)
            words_input_list_translated.append(words_IT)
            words_input_list_translated.append(words_NL)
            colu1, colu2, colu3, colu4, colu5, colu6 = st.columns(6)
            with colu1 :
                st.code(words_FR)
            with colu2 : 
                st.code(words_EN)
            with colu3 : 
                st.code(words_DE)
            with colu4 : 
                st.code(words_ES)
            with colu5 : 
                st.code(words_IT)
            with colu6 : 
                st.code(words_NL)
            st.code(words_FR + "|" + words_EN + "|" + words_DE + "|" + words_ES + "|" + words_IT + "|" + words_NL)

        
        st.markdown("Unique Translated Regex")
        unique_words_input_list_translated = list(set(words_input_list_translated))
        st.code("(" + "|".join(unique_words_input_list_translated) + ")")

        st.header("Words 1")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        wit col1 : 
          st.markdown("🇫🇷 FR 🇫🇷")
          words_1_input = st.text_input("Enter 1 word", value = "citron")
        wit col2 : 
          st.markdown("🇫🇷 FR 🇫🇷")
          words_1_input = st.text_input("Enter 1 word", value = "citron")
        wit col3 : 
          st.markdown("🇫🇷 FR 🇫🇷")
          words_1_input = st.text_input("Enter 1 word", value = "citron")
        wit col4 : 
          st.markdown("🇫🇷 FR 🇫🇷")
          words_1_input = st.text_input("Enter 1 word", value = "citron")
        wit col5 : 
          st.markdown("🇫🇷 FR 🇫🇷")
          words_1_input = st.text_input("Enter 1 word", value = "citron")
        wit col6 : 
          st.markdown("🇫🇷 FR 🇫🇷")
          words_1_input = st.text_input("Enter 1 word", value = "citron")
          
        
        
        
