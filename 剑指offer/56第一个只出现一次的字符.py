# -*- coding:utf-8 -*-

'''
题目：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
'''

# 果然还是要靠自己的想法
class Solution:
    def FirstNotRepeatingChar(self, s):
        if s is None or len(s) <= 0:
            return -1

        alist = list(s)
        blist = {}
        for i in alist:
            if i not in blist.keys():
                blist[i] = 0
            blist[i] += 1

        for i in range(len(alist)):
            if blist[alist[i]] == 1:
                return i

        return -1