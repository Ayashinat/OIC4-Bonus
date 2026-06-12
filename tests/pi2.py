import decimal
from math import ceil

NB_DECIMALES = 1_000_000
FICHIER_PI = "pi_1000000_decimal.txt"

DECIMALES_PAR_TERME = 14.181647462725477

A = 13591409
B = 545140134
C = 640320

C3_OVER_24 = C**3 // 24


def binary_split(a, b):
    if b == a + 1:
        P = -(6 * a - 5) * (2 * a - 1) * (6 * a - 1)
        Q = a**3 * C3_OVER_24
        T = P * (B * a + A)
        return P, Q, T

    m = (a + b) // 2

    P1, Q1, T1 = binary_split(a, m)
    P2, Q2, T2 = binary_split(m, b)

    P = P1 * P2
    Q = Q1 * Q2
    T = Q2 * T1 + P1 * T2

    return P, Q, T


def chudnovsky(nb_decimales):
    garde = 30

    precision = nb_decimales + garde
    decimal.getcontext().prec = precision + 5

    nb_termes = ceil(precision / DECIMALES_PAR_TERME) + 2

    print(f"Calcul avec {nb_termes} termes de la formule de Chudnovsky...")

    P, Q, T = binary_split(1, nb_termes)
    D = decimal.Decimal

    sqrt_10005 = D(10005).sqrt()
    pi = (D(426880) * sqrt_10005 * Q) / (A * Q + T)
    return pi


def ecrire_pi_dans_fichier():
    print(f"Génération de {NB_DECIMALES} décimales de π...")

    pi = chudnovsky(nb_decimales)
    pi_chaine = format(pi, f".{nb_decimales}f")
    enier, decimales = pi_chaine.split(".")

    with open(FICHIER_PI, "w", encoding="utf-8") as f:
        f.write(decimales)

    print(f"Fichier créé : {FICHIER_PI}")


if __name__ == "__main__":
    ecrire_pi_dans_fichier()