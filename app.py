import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Malick Diakhate", layout="wide")

# CSS pour diviser l'écran : 70% Blanc | 30% Noir
st.markdown("""
    <style>
    /* Supprimer les marges par défaut de Streamlit */
    .block-container {
        padding: 0rem !important;
        max-width: 100% !important;
    }
    
    /* Fond global blanc pour la partie principale */
    .stApp {
        background-color: #FFFFFF;
    }

    /* Section GAUCHE (70% - BLANC) */
    .main-col {
        background-color: #FFFFFF;
        color: #a7a7a7;
        padding: 60px;
        min-height: 100vh;
    }

    /* Section DROITE (30% - NOIR) */
    .side-col {
        background-color: #8cc8e2;
        color: #black;
        padding: 60px;
        min-height: 100vh;
    }

    /* Ajustement des couleurs de texte */
    .main-col h1, .main-col h2, .main-col h3 { color: #000000; }
    .side-col h1, .side-col h2, .side-col h3, .side-col p, .side-col li { color: #8cc8e2!important; }
    
    /* Style pour les titres de la section noire */
    .sidebar-title-custom {
        font-size: 24px;
        font-weight: bold;
        border-bottom: 2px solid #FFFFFF;
        margin-bottom: 20px;
        color: #FFFFFF;
    }

    /* Ligne de séparation dans la partie blanche */
    hr {
        border-color: #000000;
    }
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
    st.write("📅 Né le 07 Mars 2000")

    st.markdown("---")

    st.header("🎯 Objectif")
    st.write("""
    Jeune diplômé motivé et sérieux, actuellement en deuxième année de formation en Géomatique,
    je suis à la recherche d’une opportunité me permettant de mettre à profit mes compétences
    et de développer mon expérience professionnelle dans un environnement stimulant.
    """)

    st.header("🎓 Formation")
    st.markdown("### Deuxième année en Formation Géomatique (2024 - 2026)")
    st.write("SIG, cartographie, télédétection, traitement de données spatiales.")

    st.markdown("### Baccalauréat (2023) — Série L2")
    st.write("Lycée : FRATERNITE")

    st.header("💼 Expérience / Formation Professionnelle")
    st.write("""
    Pratiques en Géomatique :
    - Cartographie numérique et conception de cartes.
    - Analyse spatiale avec des outils SIG.
    - Manipulation de données de télédétection.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# COLONNE DROITE (30% - NOIR)
# -----------------------
with col2:
    st.markdown('<div class="side-col">', unsafe_allow_html=True)
    
    st.markdown("<p class='sidebar-title-custom'>Compétences</p>", unsafe_allow_html=True)
    st.markdown("""
    * Bonne capacité d’adaptation  
    * Sens de l’organisation  
    * Travail en équipe  
    * Maîtrise de Word et Excel  
    * Bases en SIG et cartographie  
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("<p class='sidebar-title-custom'>Centres d’intérêt</p>", unsafe_allow_html=True)
    st.markdown("""
    * Lecture  
    * Sport  
    * Nouvelles technologies  
    * Engagement communautaire  
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
