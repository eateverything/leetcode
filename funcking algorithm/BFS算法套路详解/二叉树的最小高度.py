# -*- coding: utf-8 -*-

'''
BFS框架
计算起点start，到终点taarget的最短路径
int BFS(Node start, Node target){
    Queue<Node> q; //核心数据结构
    Set<Node> visited;  //避免走回头路

    q.offer(start);  // 将七点放入队列
    visited.add(start);
    int step = 0;  // 记录扩散的步数

    while(q not empty){
        int sz = q.size();
        for(int i=0; i<sz; i++){
            Node cur = q.poll();
            // 划重点，在这里判断是否到达终点
            if(cur is target){
                return step;
            }
            // 将cur的相邻节点加入队列
            for(Node x: cur.adj()){
                if(x not in visited){
                    q.offer(x);
                    visited.add(x);
                }
            }
        }
        step++;
    }
}
'''

'''
leetcode 111 二叉树的最小高度

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = [root]
        depth = 1

        while q is not None:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            depth += 1

        return depth


'''
leetcode 752 打开转盘所
'''
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def neighbors(strs):  # 当前位置锁的八种状态
            for i in range(len(strs)):
                num = int(strs[i])
                for j in [-1, 1]:
                    nums = (num+j) % 10
                    yield strs[:i] + str(nums) + strs[i+1:]

        q = ['0000']
        visited = set('0000')  # 为啥用列表就不行呢
        step = 0

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                for num in neighbors(cur):
                    if num not in visited:
                        q.append(num)
                        visited.add(num)
            step += 1
        return -1
