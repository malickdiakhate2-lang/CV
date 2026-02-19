import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Malick Diakhate", layout="wide")

# CSS personnalisé
st.markdown("""
    <style>
    /* Fond général blanc */
    .main {
        background-color: white;
    }

    /* Sidebar noire */
    section[data-testid="stSidebar"] {
        background-color: black;
        color: white;
    }

    section[data-testid="stSidebar"] .css-1v0mbdj, 
    section[data-testid="stSidebar"] .css-10trblm {
        color: white;
    }

    h1, h2, h3 {
        color: #000000;
    }

    .sidebar-title {
        color: white;
        font-size: 22px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Création des colonnes 70% - 30%
col1, col2 = st.columns([7,3])

# -----------------------
# CONTENU PRINCIPAL (70%)
# -----------------------
with col1:
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

    st.write("**Deuxième année en Formation Géomatique (2024 - 2026)**")
    st.write("Formation en géomatique générale : SIG, cartographie, télédétection, traitement de données spatiales.")

    st.write("**Baccalauréat (2023) — Série L2**")
    st.write("Lycée : FRATERNITE")

    st.write("**Brevet de Fin d’Études Moyennes (2018)**")
    st.write("Collège : FRATERNITE")

    st.write("**Certificat de Fin d’Études Élémentaires (2010)**")
    st.write("École : MOBUTOU SESESEKO")

    st.header("💼 Expérience / Formation Professionnelle")

    st.write("""
    **Formation en Géomatique (2024 - 2026)**  
    - Cartographie numérique  
    - Systèmes d’Information Géographique (SIG)  
    - Télédétection  
    - Traitement et analyse de données spatiales  
    - Utilisation de logiciels spécialisés
    """)

# -----------------------
# SIDEBAR (30%)
# -----------------------
with col2:
    st.markdown("<p class='sidebar-title'>Compétences</p>", unsafe_allow_html=True)

    st.write("""
    - Bonne capacité d’adaptation  
    - Sens de l’organisation  
    - Travail en équipe  
    - Maîtrise de Word et Excel  
    - Bases en SIG et cartographie  
    """)

    st.markdown("---")

    st.markdown("<p class='sidebar-title'>Centres d’intérêt</p>", unsafe_allow_html=True)

    st.write("""
    - Lecture  
    - Sport  
    - Nouvelles technologies  
    - Engagement communautaire  
    """)
