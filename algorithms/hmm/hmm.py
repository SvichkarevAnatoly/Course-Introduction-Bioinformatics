__author__ = 'JDima'

from collections import namedtuple


def calc_hmm(hmm, top_seq, bottom_seq):
    hmm_matr = [[[0, 0, 0] for _ in range(len(top_seq) + 1)] for _ in range(len(bottom_seq) + 1)]
    for i in range(len(top_seq) + 1):
        hmm_matr[0][i] = [0, 0, 0]
    for i in range(len(bottom_seq) + 1):
        hmm_matr[i][0] = [0, 0, 0]
    hmm_matr[0][0] = [1, 0, 0]
    for j in range(1, len(top_seq) + 1):
        for i in range(1, len(bottom_seq) + 1):
            hmm_matr[i][j][0] = hmm.p[top_seq[j - 1] + bottom_seq[i - 1]] * max(hmm.a["MM"] * hmm_matr[i - 1][j - 1][0],
                                                                        hmm.a["XM"] * hmm_matr[i - 1][j - 1][2],
                                                                        hmm.a["YM"] * hmm_matr[i - 1][j - 1][1])

            hmm_matr[i][j][1] = hmm.q[bottom_seq[i - 1]] * max(hmm.a["MY"] * hmm_matr[i][j - 1][0],
                                                           hmm.a["YY"] * hmm_matr[i][j - 1][1])

            hmm_matr[i][j][2] = hmm.q[top_seq[j - 1]] * max(hmm.a["MX"] * hmm_matr[i - 1][j][0],
                                                        hmm.a["XX"] * hmm_matr[i - 1][j][2])

    print(hmm_matr)

    pass


hmm = namedtuple("HMM", ["a", "q", "p"])
hmm.a = {"MM": 0.5, "XM": 0.1, "YM": 0.8, "MX": 0.2, "XX": 0.1, "MY": 0.2, "YY": 0.1}
hmm.q = {"C": 0.25, "T": 0.25, "A": 0.25, "G": 0.25}
hmm.p = {"AA": 0.5, "CC": 0.5, "GG": 0.5, "TT": 0.5,
         "CT": 0.05, "AG": 0.05, "AT": 0.3, "GC": 0.3,
         "TC": 0.05, "GA": 0.05, "TA": 0.3, "CG": 0.3,
         "GT": 0.15, "AC": 0.15, "TG": 0.15, "CA": 0.15}

top = "TTACG"
bottom = "TAG"

calc_hmm(hmm, top, bottom)
