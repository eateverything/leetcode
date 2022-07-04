# -*- coding:utf-8 -*-

'''
题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、
10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出
任意非负整数区间中1出现的次数。
'''

# 方案一
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count

'''
//根据设定的整数位置，对n进行分割，分为两部分，高位n/i，低位n%i
//当i表示百位，且百位对应的数>=2,如n=31456,i=100，则a=314,b=56，此时百位为1的次数有a/10+1=32（最高两位0~31），每一次都包含100个连续的点，即共有(a%10+1)*100个点的百位为1
//当i表示百位，且百位对应的数为1，如n=31156,i=100，则a=311,b=56，此时百位对应的就是1，则共有a%10(最高两位0-30)次是包含100个连续点，当最高两位为31（即a=311），本次只对应局部点00~56，共b+1次，所有点加起来共有（a%10*100）+(b+1)，这些点百位对应为1
//当i表示百位，且百位对应的数为0,如n=31056,i=100，则a=310,b=56，此时百位为1的次数有a/10=31（最高两位0~30）
'''
class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        res = 0
        base = 1
        tmp = n
        while tmp:
            last = tmp % 10
            tmp = tmp / 10
            res += tmp * base
            if last == 1:
                res += n % base + 1
            elif last > 1:
                res += base
            base *= 10
        return res