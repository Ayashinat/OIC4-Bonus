from math import isqrt

NB_DECIMALES = 1_000_000
FICHIER_PI = "pi_1000000.txt"

DECIMALES_PAR_TERME = 14.181647462725477

C = 640320
TAILLE_BLOC = 4096


def binary_split(a, b):
    if b - a == 1:
        if a == 0:
            Pab = Qab = 1
        else:
            Pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
            Qab = a**3 * 10939058860032000

        Rab = Pab * (545140134 * a + 13591409)

        if a % 2:
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

    nb_termes = int(precision / DECIMALES_PAR_TERME) + 2

    print(f"Calcul avec {nb_termes} termes...")

    P1n, Q1n, R1n = binary_split(0, nb_termes)

    scale = 10**precision
    sqrt_10005 = isqrt(10005 * scale * scale)

    pi = (Q1n * 426880 * sqrt_10005) // R1n
    pi = pi // 10**garde

    return pi


def ecrire_decimales(nombre, fichier):
    base = 10**TAILLE_BLOC
    blocs = []

    while nombre:
        nombre, reste = divmod(nombre, base)
        blocs.append(reste)

    if not blocs:
        return

    premier_bloc = True
    for bloc in reversed(blocs):
        if premier_bloc:
            fichier.write(str(bloc)[1:])
            premier_bloc = False
        else:
            fichier.write(str(bloc).zfill(TAILLE_BLOC))
    
def ecrire_pi_dans_fichier():
    print(f"Génération de {NB_DECIMALES} décimales de π...")
    pi = chudnovsky(NB_DECIMALES)

    with open(FICHIER_PI, "w", encoding="utf-8") as f:
        ecrire_decimales(pi, f)

    print(f"Fichier créé : {FICHIER_PI}")


if __name__ == "__main__":
    ecrire_pi_dans_fichier()
