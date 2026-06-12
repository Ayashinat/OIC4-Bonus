# ************************************************************** #
#           *Application Streamlit autour du nombre Pi           #
#                                                                #
# Nom     : OIC Streamlit 4.3                                    #
# Fichier : pages/decimales_pi.py                                #
# Rôle    : Afficher les décimales de π                          #
# Auteurs : Wewe Maitre 24001170 et Sylvain Maitre 24002886      #
# Version : v0.1 en mai 2026                                     #
# Licence : CC-BY-SA                                             #
# Cours   : L1 OIC - 4.3 Streamlit Pi                            #
#                                                                #
# ************************************************************** #

import streamlit as st

# ====================== Config ======================
st.set_page_config(
    layout="wide",
    page_title="Décimales de π",
    page_icon="🔢"
)
#=====================================================

st.title(":gray[Les décimales de π]")
st.write(":orange[Le premier million de décimales de π]")

decimales = st.session_state.decimales

NB_COLS = 10
NB_PAR_COL = 10
NB_LIGNES = 10
BLOCS_PAR_PAGE = 10
BLOCS = 1_000_000 // (NB_COLS * NB_PAR_COL * NB_LIGNES) 
PAGES = BLOCS // BLOCS_PAR_PAGE

# On parcours d'abord les pages
for h in range(PAGES):
    page = []
    st.write(f"Page {h + 1} sur {PAGES}")
    # On parcourt les blocs de chaque page bloc par bloc
    for i in range(BLOCS_PAR_PAGE):
        numero_bloc = h * BLOCS_PAR_PAGE + i
        # Calcul de la position du début du bloc dans les décimales
        debut_bloc = numero_bloc * NB_COLS * NB_PAR_COL * NB_LIGNES
        bloc = []
        # On parcourt chaque bloc ligne par ligne
        for j in range(NB_LIGNES):
            # Calcul de la position du début de la ligne dans les décimales
            debut_ligne = debut_bloc + j * NB_COLS * NB_PAR_COL
            ligne = [
                decimales[debut_ligne + k * NB_COLS : debut_ligne + (k + 1) * NB_COLS]
                for k in range(NB_PAR_COL)
            ]
            # On assemble la ligne et on l'ajoute au bloc
            bloc.append("  ".join(ligne))
        # page.append(f"[{numero_bloc + 1}] Décimales de {debut_bloc + 1} à {debut_bloc + NB_COLS * NB_PAR_COL * NB_LIGNES} :")
        # On ajoute le bloc à la page
        page.extend(bloc)
        # Un petit séparateur
        page.append("")
    # On assemble les blocs dans une page et on l'affiche en tant que code
    st.code("\n".join(page), language=None)
    # Séparateur de pages
    st.write("")
