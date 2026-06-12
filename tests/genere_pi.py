# ************************************************************** #
#           *Application Streamlit autour du nombre Pi           #
#                                                                #
# Nom     : OIC Streamlit 4.3                                    #
# Fichier : genere_pi.py                                         #
# Rôle    : Générer les décimales de PI dans un fichier          #
# Auteurs : Wewe Maitre 24001170 et Sylvain Maitre 24002886      #
# Version : v0.1 en mai 2026                                     #
# Licence : CC-BY-SA                                             #
# Cours   : L1 OIC - 4.3 Streamlit Pi                            #
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
from math import isqrt

sys.set_int_max_str_digits(0)

C = 640320
C3_OVER_24 = C**3 // 24


def binary_split(a, b):
    if b - a == 1:
        if a == 0:
            P = 1
            Q = 1
        else:
            P = (6*a - 5) * (2*a - 1) * (6*a - 1)
            Q = a**3 * C3_OVER_24

        T = P * (13591409 + 545140134 * a)

        if a % 2:
            T = -T

        return P, Q, T

    m = (a + b) // 2

    P1, Q1, T1 = binary_split(a, m)
    P2, Q2, T2 = binary_split(m, b)

    P = P1 * P2
    Q = Q1 * Q2
    T = T1 * Q2 + P1 * T2

    return P, Q, T


def pi_decimals(n):
    guard = 10
    precision = n + guard

    terms = int(precision / 14.181647462725477) + 2

    P, Q, T = binary_split(0, terms)

    scale = 10**precision
    sqrt_10005 = isqrt(10005 * scale * scale)

    pi_scaled = (Q * 426880 * sqrt_10005) // T

    s = str(pi_scaled)

    integer_part = s[:-precision]
    decimal_part = s[-precision:-guard]

    # return integer_part + "." + decimal_part
    return decimal_part


def ecrire_pi_dans_fichier():
    with open("pi_1000000.txt", "w") as f:
        f.write(pi_decimals(1000000))


if __name__ == "__main__":
    ecrire_pi_dans_fichier()