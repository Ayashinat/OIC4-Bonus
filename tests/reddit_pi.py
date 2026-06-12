from math import ceil, log2
from gmpy2 import get_context, mpfr, mpz, sqrt


FICHIER_PI = "pi_1000000.txt"
NB_DECIMALES = 1000000



A = mpz(13591409)
B = mpz(545140134)
C = mpz(640320)
C3_OVER_24 = (C**3) // 24

def bs(a: int, b: int):
    if b - a == 1:
        if a == 0:
            P = Q = mpz(1)
        else:
            a_mpz = mpz(a)
            P = (6*a_mpz-5) * (2*a_mpz-1) * (6*a_mpz-1)
            Q = a_mpz ** 3 * C3_OVER_24
        T = (-1) ** a * P * (A + B * a)
        return P, Q, T
    m = (a + b) // 2
    P1, Q1, T1 = bs(a, m)
    P2, Q2, T2 = bs(m, b)
    P = P1 * P2
    Q = Q1 * Q2
    T = T1 * Q2 + P1 * T2
    return P, Q, T

def pi_chudnovsky(bits: int) -> mpfr:
    get_context().precision = bits
    P, Q, T = bs(0, bits // 47 + 1) # Chaque terme donne ~47 bits de pi
    return mpfr(426880) * sqrt(mpfr(10005)) * mpfr(Q) / mpfr(T)


def ecrire_pi_dans_fichier():
    bits = ceil(NB_DECIMALES * log2(10)) + 64 # 64 bits de garde

    pi = pi_chudnovsky(bits)

    pi_string = format(pi, f".{NB_DECIMALES}f")
    s0, s1 = pi_string.split(".")
    decimales = s1[:NB_DECIMALES]


    with open(FICHIER_PI, "w") as f:
        f.write(decimales)

if __name__ == "__main__":
    ecrire_pi_dans_fichier()
