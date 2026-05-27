# Fichier : app.py
# Auteur : Wewe MAITRE (XIA) // Sylvain MAITRE
# Date : MAI 2026
# Exercice 4.3 Application streamlit des consignes en brain fuck

import streamlit as st
import datetime
# import math

st.title("OIC Streamlit 4.3 bonus")
st.subheader("Consigne 1")
st.write(
    "Trouver une date de naissance dans le nombre PI"
)


def cherche_date_pi(naissance):
    with open("pi_1000000.txt", "r") as f:
        pi = f.read().strip()

    pi_digits = pi.split(".")[1]
    
    if naissance in pi_digits:
        return f"Votre date de naissance {naissance} est présente dans les décimales de PI !"
    else:
        return f"Votre date de naissance {naissance} n'est pas présente dans les décimales de PI."

naissance = st.text_input("Entrez votre date de naissance (format JJMMYY) :").strip()

if naissance:
    result = cherche_date_pi(naissance)
    st.write(result)


st.subheader("Consigne 2")
st.write(
    "Dans un champ texte, affichez le jour de naissance correspondant"
)

if naissance:
    try:
        date_naissance = datetime.datetime.strptime(naissance, "%d%m%y")

        jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
        jour_semaine = jours[date_naissance.weekday()]

        st.write(f"Le jour de naissance correspondant est : {jour_semaine}")
        st.write(f"Votre date de naissance est : {date_naissance.strftime('%d %B %Y')}")
        st.write(f"Votre date de naissance est : {date_naissance}")
    except ValueError:
        st.error("Veuillez entrer une date valide au format JJMMYY, par exemple 010104.")


st.subheader("Consigne 3")
st.write(
    "Calculez la somme des 20 premieres decimales de PI, puis dans un second la somme des 12² premieres decimales de PI"
)

st.write("avec le fichier pi_1000000.txt généré par genere_pi.py")
with open("pi_1000000.txt", "r") as f:
    pi_decimales = f.read().split(".")[1]

vingt_premieres_decimales = pi_decimales[:20]
somme_20_decimales = sum(int(chiffre) for chiffre in vingt_premieres_decimales)

cent_quarante_quatre_decimales = pi_decimales[:12**2]
somme_144_decimales = sum(int(chiffre) for chiffre in cent_quarante_quatre_decimales)

st.write(f"Les 20 premieres decimales de PI sont : {vingt_premieres_decimales}")
st.write(f"La somme des 20 premieres decimales de PI est : {somme_20_decimales}")


st.write(f"Les 12² premieres decimales de PI sont : {cent_quarante_quatre_decimales}")
st.write(f"La somme des 12² premieres decimales de PI est : {somme_144_decimales}")

st.subheader("Consigne 4")


st.video("https://youtu.be/GnZQOb9YNV4?si=yc7A5ocfgJAIy2bN")