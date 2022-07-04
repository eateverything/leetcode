# -*- coding: utf-8 -*-

'''
KMP算法
'''
class KMP(object):
    def search(self, txt, pat):
        M = len(pat)
        N = len(txt)
        dp = [[0] * 256 for _ in range(M)]
        dp[0][ord(pat[0])] = 1
        X = 0
        for j in range(1, M):
            for c in range(256):
                dp[j][c] = dp[X][c]
            dp[j][ord(pat[j])] = j + 1
            X = dp[X][ord(pat[j])]

        j = 0
        for i in range(N):
            j = dp[j][ord(txt[i])]
            if j == M:
                return i - M + 1

        return -1


class kmp(object):
    def search(self, s, pattern):
        next = self.getNext(pattern)
        print(next)
        j = 0
        for i in range(len(s)):
            while j > 0 and pattern[j] != s[i]:
                j = next[j]
            if pattern[j] == s[i]:
                j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
        return -1

    def getNext(self, pattern):
        next = [0] * len(pattern)
        j = 0
        for i in range(2, len(pattern)):
            while j != 0 and pattern[j] != pattern[i-1]:
                j = next[j]
            if pattern[j] == pattern[i-1]:
                j += 1
            next[i] = j
        return next


if __name__ == "__main__":
    pat = 'aaab'
    txt = 'aaacbbbbcaaab'
    kmp1 = KMP()
    kmp2 = kmp()
    pos1 = kmp1.search(txt, pat)
    pos2 = kmp2.search(txt, pat)
    print(pos1)
    print(pos2)