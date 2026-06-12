# ************************************************************** #
#           *Application Streamlit autour du nombre Pi           #
#                                                                #
# Nom     : OIC Streamlit 4.3                                    #
# Fichier : genere_pi.py                                         #
# Rôle    : Générer les décimales de PI dans un fichier          #
# Auteurs : Wewe Maitre 24001170 et Sylvain Maitre 24002886      #
# Version : v0.2 le 3 juin 2026                                  #
# Licence : CC-BY-SA                                             #
# Cours   : L1 OIC - 4.3 Streamlit Pi                            #
# Sources : Wikipedia, stackoverflow...                          #
#                                                                #
# Utilisation : python3 genere_pi.py                             #
#                                                                #
#    ou                                                          #
#                                                                #
# Importé dans une application :                                 #
#    from genere_pi import ecrire_pi_dans_fichier                #
#    ecrire_pi_dans_fichier()                                    #
#                                                                #
# ************************************************************** #


import sys
import time
from math import isqrt


# 1 Mo ça ne mange pas de pain, on peut lever la limite
sys.set_int_max_str_digits(0)


NB_DECIMALES = 1_000_000
FICHIER_PI = "pi_1000000.txt"

C = 640320

# Division binaire
def binary_split(a, b):
    if b - a == 1:
        if a == 0:
            Pab = Qab = 1
        else:
            Pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
            Qab = a * a * a * 10939058860032000
        Rab = Pab * (545140134 * a + 13591409)
        if a & 1:
            Rab = -Rab
        return Pab, Qab, Rab
    m = (a + b) // 2
    Pam, Qam, Ram = binary_split(a, m)
    Pmb, Qmb, Rmb = binary_split(m, b)
    Pab = Pam * Pmb
    Qab = Qam * Qmb
    Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(nb_decimales):
    garde = 10
    precision = nb_decimales + garde
    nb_termes = int(precision / 14.181647462725477) + 2
    print(f"Calcul avec {nb_termes} termes...")
    # P : produit des facteur du numérateur
    # Q : produit des facteur du dénominateur
    # R : numérateur de la somme partielle mise au même dénominateur
    P1n, Q1n, R1n = binary_split(0, nb_termes)
    sqrt_10005 = isqrt(10005 * 10 ** (2 * precision))
    pi = (Q1n * 426880 * sqrt_10005) // R1n
    pi = pi // 10**garde
    return pi


def ecrire_pi_dans_fichier():
    print(f"Génération de {NB_DECIMALES} décimales de π...")
    pi = chudnovsky(NB_DECIMALES)
    with open(FICHIER_PI, "w", encoding="utf-8") as f:
        f.write(str(pi)[1:])
    print(f"Fichier créé : {FICHIER_PI}")


if __name__ == "__main__":
    time_depart = time.time()
    ecrire_pi_dans_fichier()
    time_fin = time.time()
    print(f"Temps de génération : {time_fin - time_depart:.2f} secondes")
