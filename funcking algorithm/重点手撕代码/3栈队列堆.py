# -*- coding: utf-8 -*-

# leetcode 225 用队列实现栈
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.topElem = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.topElem = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.queue)
        while size > 2:
            self.queue.append(self.queue.pop(0))
            size -= 1
        self.topElem = self.queue[0]
        self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topElem

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# leetcode 232 用栈实现队列
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


# leetcode 155 最小栈（包含min函数的栈）
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []  # 存放每个位置当前的最小值

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minStack == [] or x < self.getMin():  # 列表为空 写 is None 不管用
            self.minStack.append(x)
        else:
            self.minStack.append(self.getMin())

    def pop(self) -> None:
        if self.stack == [] or self.minStack == []:
            return None
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# 计算器
class Solution:
    # leetcode 227 基本计算器II，超出时间限制
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0
            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = num * 10 + int(c)
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                    sign = c
                    num = 0
            return sum(stack)
        return helper(list(s))

    # leetcode 224 基本计算器，又是同样的超出时间限制
    def calculate2(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = helper(s)
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)

                    sign = c
                    num = 0
                if c == ')':
                    break
            return sum(stack)
        return helper(list(s))

    # leetcode 215 数组中的第k个最大元素
    # 快排的变种
    def findKthLargest(self, nums: list[int], k: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            i = low
            j = high - 1
            tmp = nums[low]
            # 快排思想：比tmp大的都放在前边，小的都放在后边
            while i <= j:
                while i <= j and nums[i] >= tmp:
                    i += 1
                while i <= j and nums[j] < tmp:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[low], nums[j] = nums[j], nums[low]

            if j == k-1:
                return nums[j]
            elif j < k-1:
                low = j + 1
            else:
                high = j


# leetcode 295 数据流中的中位数
# 大顶堆和小顶堆的配合
# python只有小顶堆，没有大顶堆，所以元素取反，小顶堆秒变大顶堆
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = []
        self.max_h = []
        heapify(self.min_h)
        heapify(self.max_h)

    def addNum(self, num: int) -> None:
        # 来一个数先放到小顶堆里，然后把小顶堆的对顶放到大顶堆
        # 同时保证小顶堆>=大顶堆，不论是个数还是数值
        heappush(self.min_h, num)
        heappush(self.max_h, -heappop(self.min_h))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h, -heappop(self.max_h))

    def findMedian(self) -> float:
        if len(self.min_h) == len(self.max_h):
            return (self.min_h[0] - self.max_h[0]) / 2
        else:
            return self.min_h[0] / 1


    def MaxHeap(self, alist):
        length = len(alist)
        if alist is None or length <=0:
            return
        if length == 1:
            return alist

        for i in range(length // 2 - 1, -1, -1):
            k = i
            tmp = alist[k]
            heap = False

            while not heap and 2 * k < length - 1:
                index = 2 * k + 1  # 左孩子
                if index < length - 1:  # 确保有右孩子
                    if alist[index] < alist[index+1]:
                        index += 1
                if tmp >= alist[index]:
                    heap = True
                else:
                    # 父节点和最大那个孩子交换，继续
                    alist[k] = alist[index]
                    k = index
            alist[k] = tmp


    def MinHeap(self, alist):
        length = len(alist)
        if alist is None or length <= 0:
            return
        if length == 1:
            return alist

        for i in range(length // 2 - 1, -1, -1):
            k = i
            tmp = alist[k]
            heap = False

            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index+1]:
                        index += 1
                if tmp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = tmp


