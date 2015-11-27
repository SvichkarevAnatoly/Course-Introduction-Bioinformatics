import numpy as np
import pairalign as pa

match = 2
mismatch = -1
d = -2


def na(s1, i):
    return s1.count(s1[i])


def nb(s2, j):
    return s2.count(s2[j])


def ng(s1, s2):
    return s1.count('-') + s2.count('-')


def ngd(s1, s2):
    count = ng(s1, s2)
    return 1 if count == 0 else count * d


def sab(i, j, s1, s2):
    return match if s1[i] == s2[j] else mismatch


def srand(s1, s2):
    L = len(s1)
    result = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == '-' or s2[j] == '-':
                continue
            result += sab(i, j, s1, s2) * na(s1, i) * nb(s2, j)
    return float(result) * ngd(s1, s2) / L


def smax(s1, s2):
    a1 = pa.alignment(s1, s1)
    a2 = pa.alignment(s2, s2)
    return float(a1[2] + a2[2]) / 2


def dij(s_ij, s_rand, s_max):
    return -np.log(float(s_ij - s_rand) / (s_max - s_rand))


if __name__ == "__main__":
    seqs = [
        "GCAAAGC",
        "GTAGAATC",
        "GCCTG",
        "CCATC"
    ]

    for i in range(len(seqs)):
        for j in range(i + 1, len(seqs)):
            a1, a2, score = pa.alignment(seqs[i], seqs[j])
            print str(i+1) + ": " + a1
            print str(j+1) + ": " + a2
            print "score: " + str(score)
            s_max = smax(seqs[i], seqs[j])
            print "smax: " + str(s_max)
            s_rand = srand(a1, a2)
            print "srand: " + str(s_rand)
            print "D" + str(i+1) + str(j+1) + ": " +\
                  str(dij(score, s_rand, s_max)) + "\n"
