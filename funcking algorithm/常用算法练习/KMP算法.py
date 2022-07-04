# -*- coding: utf-8 -*-

class KMP(object):
    def kmp(self, s, patten):
        def get_next(patten):
            next = [0] * len(patten)
            j = 0
            for i in range(2, len(patten)):
                while j != 0 and patten[j] != patten[i-1]:
                    j = next[j]
                if patten[j] == patten[i-1]:
                    j += 1
                next[i] = j
            return next

        next = get_next((patten))
        j = 0
        for i in range(len(s)):
            while j > 0 and s[i] != patten[j]:
                j = next[j]
            if s[i] == patten[j]:
                j += 1
            if j == len(patten):
                return i - len(patten) + 1
        return -1


if __name__ == "__main__":
    pat = 'aaab'
    txt = 'aaacbbbbcaaab'
    kmp1 = KMP()
    pos1 = kmp1.kmp(txt, pat)
    print(pos1)