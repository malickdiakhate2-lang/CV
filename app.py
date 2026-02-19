import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Malick Diakhate", layout="wide")

# CSS pour centrer le texte sur le fond
st.markdown("""
    <style>
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }

    /* Fond global */
    .stApp {
        background-color: #FFFFFF;
    }

    /* Section GAUCHE (70% - BLANC) */
    .main-col {
        background-color: #FFFFFF;
        color: #000000;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center; /* centre verticalement */
        align-items: flex-start; /* aligne à gauche */
        padding: 60px;
    }

    /* Section DROITE (30% - BLEU CLAIR) */
    .side-col {
        background-color: #8cc8e2;
        color: #FFFFFF;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center; /* centre verticalement */
        align-items: flex-start;
        padding: 60px;
    }

    /* Titres */
    .main-col h1, .main-col h2, .main-col h3 { color: #000000; }
    .side-col h1, .side-col h2, .side-col h3, .side-col p, .side-col li { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# Création des colonnes (7:3)
col1, col2 = st.columns([7, 3], gap="small")

# -----------------------
# COLONNE GAUCHE (70% - BLANC)
# -----------------------
with col1:
    st.markdown('<div class="main-col">', unsafe_allow_html=True)
    st.title("Malick Diakhate")
    st.subheader("📍 Keur Massar, Sénégal")
    st.write("📧 malickdiakhate123@gmail.com")
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# COLONNE DROITE (30% - BLEU CLAIR)
# -----------------------
with col2:
    st.markdown('<div class="side-col">', unsafe_allow_html=True)
    st.header("Compétences")
    st.write("- SIG\n- Webmapping\n- Python")
    st.markdown('</div>', unsafe_allow_html=True)
