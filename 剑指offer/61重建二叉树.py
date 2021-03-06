# -*- coding:utf-8 -*-

'''
题目：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

# 思路：前序遍历第一个是根节点，中序遍历找到根节点后，左右各为左右子树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        print(val)
        root.left = self.reConstructBinaryTree(pre[1: val+1], tin[: val])
        root.right = self.reConstructBinaryTree(pre[val+1:], tin[val+1:])

        return root


if __name__ == "__main__":
    Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])