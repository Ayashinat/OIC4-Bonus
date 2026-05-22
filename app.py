import streamlit as st
import datetime

st.title("OIC Streamlit 4.3 bonus")
st.subheader("Consigne 1")
st.write(
    "Trouver une date de naissance dans le nombre PI"
)

def cherche_date_pi(naissance):
    with open("pi_1000000.txt", "r") as f:
        pi_digits = f.read().replace(".", "")  # Remove the decimal point

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

