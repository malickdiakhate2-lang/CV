import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Malick Diakhate", layout="wide")

# CSS personnalisé avec dégradé
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fdfbfb, #ebedee);
        color: #000000;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #000000, #434343);
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

    .divider {
        height: 4px;
        background: linear-gradient(to right, #000000, #8cc8e2);
        margin: 25px 0;
        border-radius: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# Création des colonnes
col1, col2 = st.columns([7,3])

# -----------------------
# CONTENU PRINCIPAL (70%)
# -----------------------
with col1:
    st.title("Malick Diakhate")
    st.subheader("📍 Keur Massar, Sénégal")
    st.write("📧 malickdiakhate123@gmail.com")
    st.write("📅 Né le 07 Mars 2000")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # 🔹 Section Profil
    st.header("👤 Profil")
    st.write("""
    Étudiant en Géomatique, passionné par la cartographie numérique et les technologies SIG.
    Curieux, motivé et rigoureux, je cherche à mettre mes compétences en analyse spatiale,
    webmapping et traitement de données au service de projets innovants.
    """)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.header("🎯 Objectif")
    st.write("""
    Jeune diplômé motivé et sérieux, actuellement en deuxième année de formation en Géomatique,
    je suis à la recherche d’une opportunité me permettant de mettre à profit mes compétences
    et de développer mon expérience professionnelle dans un environnement stimulant.
    """)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.header("🎓 Formation")
    st.write("Deuxième année en Formation Géomatique (2024 - 2026)")
    st.write("Formation en géomatique générale : SIG, cartographie, télédétection, traitement de données spatiales.")
    st.write("Baccalauréat (2023) — Série L2, Lycée FRATERNITE")
    st.write("Brevet de Fin d’Études Moyennes (2018), Collège FRATERNITE")
    st.write("Certificat de Fin d’Études Élémentaires (2010), École MOBUTOU SESESEKO")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.header("💼 Expérience / Formation Professionnelle")
    st.write("""
    Formation en Géomatique (2024 - 2026)  
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

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("<p class='sidebar-title'>Centres d’intérêt</p>", unsafe_allow_html=True)
    st.write("""
    - Lecture  
    - Sport  
    - Nouvelles technologies  
    - Engagement communautaire  
    """)
