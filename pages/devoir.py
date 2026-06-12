# ************************************************************** #
#           *Application Streamlit autour du nombre Pi           #
#                                                                #
# Nom     : OIC Streamlit 4.3                                    #
# Fichier : pages/accueil.py                                     #
# Rôle    : Page principale - consignes                          #
# Auteurs : Wewe Maitre 24001170 et Sylvain Maitre 24002886      #
# Version : v0.1 en mai 2026                                     #
# Licence : CC-BY-SA                                             #
# Cours   : L1 OIC - 4.3 Streamlit Pi                            #
#                                                                #
# ************************************************************** #

import streamlit as st
import datetime

st.title(":gray[Trouver une date dans **Π**]", text_alignment="center")
st.write("")

# On récupère les décimales de π depuis la session
decimales = st.session_state.decimales

# ==============================================================================
#                                  CONSIGNE 1
# ==============================================================================

st.subheader(":orange[Consigne 1]")
st.write(r"Créez une application Streamlit, la même que celle de l’exercice 4.2 ou une autre, qui recherche dans le premier million de décimales de $\pi$ la présence d’une date de naissance saisie par l’utilisateur")

# Test de validité de la date de naissance
def date_naissance_valide(naissance):
    # Si la date n'a pas la bonne longueur ou contient des caractères non numériques
    # On sait d'office qu'elle n'est pas valide
    if len(naissance) != 6 or not naissance.isdigit():
        return None
    try:
        # Si le format est correct, on retourne un objet datetime
        return datetime.datetime.strptime(naissance, "%d%m%y")
    except ValueError:
        # Si la date n'est pas valide, on retourne None
        return None

# Recherche de la date de naissance dans les décimales de π
def cherche_date_pi(naissance):
    # Si la chaîne "naissance" est présente dans la chaîne "decimales"
    if naissance in decimales:
        return "est"
    else:
        return "n'est pas"

# Création d'un champ inputbox paramétré car date_input ne permet pas le format JJMMYY
naissance = st.text_input("Entrez votre date de naissance :",
    # Nombre maximum de caractères à saisir
    max_chars=6,
    # Placeholder pour indiquer le format attendu
    placeholder="JJMMAA",
    # Aide pour l'utilisateur
    help="Entrez votre date de naissance au format JJMMYY sans séparateurs, par exemple 010280 pour le 1er février 1980.",
    # Icone pour le champ de saisie
    icon=":material/calendar_month:"
)

date_naissance = date_naissance_valide(naissance)

# Si une date est présente mais invalide
if naissance and date_naissance is None:
    st.error("La date de naissance saisie n'est pas valide.")
# Et quelle est valide
elif date_naissance is not None:
    presence = cherche_date_pi(naissance)
    st.write(f"Votre date de naissance {naissance} {presence} présente dans les décimales de pi.")


# ==============================================================================
#                                  CONSIGNE 2
# ==============================================================================

st.divider()
st.subheader(":orange[Consigne 2]")
st.write("Dans un champ texte, après l'avoir calculé avec Python ou obtenu en ligne, affichez le jour de naissance correspondant :")

# Si une date de naissance valide a été saisie
if date_naissance is not None:
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    # Piocher le jour correspondant au numéro
    jour_semaine = jours[date_naissance.weekday()]
    # Affichage du jour de naissance
    st.info(f"Le jour de naissance correspondant est : **{jour_semaine}**")
    # Affichage de la date de naissance formattée
    st.write(f"Votre date de naissance est : {date_naissance.strftime('%d %B %Y')}")
else:
    st.info("Il n'y a pas de date de naissance saisie pour le moment.")


# ==============================================================================
#                                  CONSIGNE 3
# ==============================================================================

st.divider()
st.subheader(":orange[Consigne 3]")
st.write(r"Dans un autre champ texte, calculez la somme des 20 premières décimales de $\pi$, puis dans un second la somme des 12$^2$ premières décimales. Que remarquez-vous ?")

st.write("Calculs réalisés à partir du million de décimales de π stocké du ficher :")

# Extraire les 20 premières décimales
vingt_premieres_decimales = decimales[:20]

# Faire la somme des 20 premieres décimales en transformant chaque caractère en entier
somme_20_decimales = sum(int(chiffre) for chiffre in vingt_premieres_decimales)

# Extraire les 12² premières décimales
cent_quarante_quatre_decimales = decimales[:12**2]

# Faire la somme des 12² premières décimales en transformant chaque caractère en entier
somme_144_decimales = sum(int(chiffre) for chiffre in cent_quarante_quatre_decimales)

st.write(f"Les 20 premières décimales de pi sont :")
st.info(f"{vingt_premieres_decimales}")

st.write(f"La somme des 20 premières décimales de pi est :")
st.success(f"{somme_20_decimales}")

st.write(f"Les 12² premières décimales de pi sont :")
st.info(f"{cent_quarante_quatre_decimales}")

st.write(f"La somme des 12² premières décimales de pi est :")
st.success(f"{somme_144_decimales}")


# ==============================================================================
#                                  CONSIGNE 4
# ==============================================================================

st.divider()
st.subheader(":orange[Consigne 4]")
st.write(r"Insérez dans votre application une vidéo prise en ligne qui montre que la somme de tous les nombres entiers naturels est égale à $-\frac{1}{12}$ :")

st.video("https://youtu.be/GnZQOb9YNV4?si=yc7A5ocfgJAIy2bN")
