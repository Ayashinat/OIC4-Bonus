# ************************************************************** #
#           *Application Streamlit autour du nombre Pi           #
#                                                                #
# Nom     : OIC Streamlit 4.3                                    #
# Fichier : app.py                                               #
# Rôle    : Application Streamlit autour du nombre Pi            #
# Auteurs : Wewe Maitre 24001170 et Sylvain Maitre 24002886      #
# Version : v0.1 en mai 2026                                     #
# Licence : CC-BY-SA                                             #
# Cours   : L1 OIC - 4.3 Streamlit Pi                            #
#                                                                #
# Utilisation : prévue avec make                                 #
#                                                                #
# ************************************************************** #

import streamlit as st
import os
from genere_pi import ecrire_pi_dans_fichier


FICHIER = "pi_1000000.txt"


# ====================== Config ======================
st.set_page_config(
    page_title="OIC Streamlit 4.3",
    page_icon="🎂",
    layout="centered"
)
#=====================================================


# Si le fichier des décimales n'existe pas encore :
if not os.path.exists(FICHIER):
    # Afficher un spinner pendant la génération des décimales
    with st.spinner("Génération des décimales de π en cours, merci de patienter..."):
        # Appeler la fonction génératrice
        ecrire_pi_dans_fichier()
    st.rerun()


# Si les décimales ne sont pas dans la sessions
if "decimales" not in st.session_state:
    # Ouvrir le fichier des décimales en lecture seule
    with open(FICHIER, "r") as f:
        # Lires les décimales et les stocker dans la session
        # En faisant confiance que le fichier n'a pas été corrompu d'une manière quelconque
        st.session_state.decimales = f.read()


# Barre de nafigation gauche
pg = st.navigation([
    st.Page("pages/devoir.py", title="Devoir", icon="🎂"),
    st.Page("pages/decimales_pi.py", title="Décimales de π", icon="🔢"),
])


# Afficher la page sélectionnée
pg.run()
