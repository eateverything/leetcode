# -*- coding: utf-8 -*-

'''
leetcode 651 4键键盘
可以有A，C-A，C-C，C-A，C-V，四种操作，求N次操作后屏幕最多有多少个A
'''
# 第一种思路
# 确定状态和选择
# 选择有4种：A，C-A，C-C，C-A，C-V
# 状态可以有3种：1）按键剩余次数n，2）当前屏幕上A的个数a_num，3）当前剪切板中A的个数copy
# 状态转移：dp(n, a_num, copy) =
# 1）dp(n-1, a_num+1, copy): 按下一个A，次数少一次，A的个数加1；
# 2）dp(n-1, a_num+copy, copy): C-V
# 3）dp(n-2, a_num, a_num): C-A，C-C
def maxA(N: int) -> int:
    def dp(n, a_num, copy):
        if n <= 0:
            return a_num
        return max(dp(n-1, a_num, copy),
                   dp(n-1, a_num+copy, copy),
                   dp(n-2, a_num, a_num))
    dp(N, 0, 0)


# 备忘录消除重复子问题
def maxA(N: int) -> int:
    memo = dict()

    def dp(n, a_num, copy):
        if n <= 0:
            return a_num
        if (n, a_num, copy) in memo:
            return memo[(n, a_num, copy)]
        memo[(n, a_num, copy)] = max(dp(n-1, a_num, copy),
                   dp(n-1, a_num+copy, copy),
                   dp(n-2, a_num, a_num))
        return memo[(n, a_num, copy)]
    dp(N, 0, 0)


# 第二种思路
# 确定状态和选择
# 选择有4种：A，C-A，C-C，C-A，C-V
# 状态只有一个：剩余按键次数，dp[i]表示第i次操作后屏幕上最多有多少个A
# 状态转移：
# 1)按一次A dp[i] = dp[i-1] + 1
# 2)C-A，C-C，之后若干次C-V，然后不断循环
def maxA(N: int) -> int:
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        # 按下A键
        dp[i] = dp[i-1] + 1
        # 在第j次按键的时候开始一直C-V,j至少是2，因为前面要有C-A，C-C的操作
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j-2]*(i - j + 1))
    return dp[N]
