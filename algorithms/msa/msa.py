s1 = "GTAGAATC"
s2 = "GCA-AAGC"

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


print srand(s1, s2)
