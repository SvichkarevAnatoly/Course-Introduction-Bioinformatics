# coding=utf-8
import sys

penalty = 2


def lcs_backtrack(v, w):
    v_len = len(v)
    w_len = len(w)
    s = [[0] * (w_len + 1) for _ in range(v_len + 1)]
    backtrack = [[0] * w_len for _ in range(v_len)]

    for i in range(1, w_len + 1):
        s[0][i] = -i * penalty
    for i in range(1, v_len + 1):
        s[i][0] = -i * penalty

    for i in range(1, v_len + 1):
        for j in range(1, w_len + 1):
            s[i][j] = max(
                s[i - 1][j] - penalty,
                s[i][j - 1] - penalty,
                s[i - 1][j - 1] + (2 if v[i - 1] == w[j - 1] else -1))

            if s[i][j] == s[i - 1][j] - penalty:
                backtrack[i - 1][j - 1] = "↓"
            elif s[i][j] == s[i][j - 1] - penalty:
                backtrack[i - 1][j - 1] = "→"
            elif s[i][j] == s[i - 1][j - 1] + (
            2 if v[i - 1] == w[j - 1] else -1):
                backtrack[i - 1][j - 1] = "↘"

    # for i in range(v_len + 1):
    #     for j in range(w_len + 1):
    #         sys.stdout.write(str(s[i][j]) + " ")
    #     sys.stdout.write("\n")

    return backtrack, s[v_len][w_len]


def output_lcs(backtrack, v, w, i, j, alignment):
    while i >= 0 and j >= 0:
        if backtrack[i][j] == "↘":
            alignment[v].append(v[i])
            alignment[w].append(w[j])
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            alignment[v].append(v[i])
            alignment[w].append('-')
            i -= 1
        else:
            alignment[v].append('-')
            alignment[w].append(w[j])
            j -= 1
    while j < 0 <= i:
        alignment[v].append(v[i])
        alignment[w].append('-')
        i -= 1
    while i < 0 <= j:
        alignment[v].append('-')
        alignment[w].append(w[j])
        j -= 1
    alignment[v].reverse()
    alignment[w].reverse()


def parse_input_txt(file_name):
    with open(file_name) as f:
        v = f.readline().strip()
        w = f.readline().strip()
    return v, w


def alignment(v, w):
    backtrack, score = lcs_backtrack(v, w)
    align = {v: [], w: []}
    v_last, w_last = len(v) - 1, len(w) - 1
    output_lcs(backtrack, v, w, v_last, w_last, align)

    align_v = "".join(align[v])
    align_w = "".join(align[w])
    return align_v, align_w, score


def main():
    # file_name = sys.argv[1]
    # v, w = parse_input_txt(file_name)
    w = "GCAAGC"
    v = "GTAGAATC"

    backtrack, score = lcs_backtrack(v, w)
    alignment = {v: [], w: []}
    v_last, w_last = len(v) - 1, len(w) - 1
    output_lcs(backtrack, v, w, v_last, w_last, alignment)
    alignment_text = "".join(alignment[v]) + '\n' + "".join(alignment[w])
    print str(score) + '\n' + alignment_text


if __name__ == "__main__":
    main()
