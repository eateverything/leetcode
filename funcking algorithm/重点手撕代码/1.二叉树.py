# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # leetcode 114 二叉树转为链表
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root
        while p.right is not None:
            p = p.right
        p.right = right

        return root

    # leetcode 112 路径总和
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return sum == root.Val

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    # leetcode 236 二叉树的最近公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if p == root or q == root:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        return l if l is not None else r

    # leetcode 235 二叉搜索树的最近公共祖先
    # 二叉搜索树的性质，根节点比左节点大，比右节点小
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

    # 144 二叉树的前序遍历
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        result = []
        stack = []

        while stack or root:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return result

    # leetcode 94 二叉树中序遍历
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        result = list()

        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    # 145 二叉树的后向遍历
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        result = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                # 有左孩子就遍历做孩子，否则右孩子
                root = root.left if root.left else root.right
            root = stack.pop()
            result.append(root.val)

            # 此处说明他是从左孩子回来的，还要去遍历右孩子
            if stack and stack[-1].left == root:
                root = stack[-1].right
            else:
                root = None
        return result

    # leetcode 226 翻转二叉树
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # leetcode 654 最大二叉树
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        def build(nums, lo, hi):
            # 递归要先确定终止条件
            if lo > hi:
                return None
            index = -1
            maxval = -float('inf')
            # 获取数组中的最大值以及对应的索引
            for i in range(lo, hi+1):
                if nums[i] > maxval:
                    index = i
                    maxval = nums[i]
            # 构造根节点
            root = TreeNode(maxval)
            # 递归生成左子树
            root.left = build(nums, lo, index-1)
            # 递归生成右子树
            root.right = build(nums, index+1, hi)
            return root

        if nums is None or len(nums) <= 0:
            return None
        return build(nums, 0, len(nums)-1)

    # leetcode 105 从前序遍历和中续遍历结果构造二叉树
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # 要充分了解二叉树遍历，以及前序遍历和中序遍历的联系和特点
        def build(preorder, preStart, preEnd, inorder, inStart, inEnd):
            # 一定要记得终止条件
            if preStart > preEnd or inStart > inEnd:
                return None
            rootVal = preorder[preStart]
            index = 0
            # 在中序遍历中找到根节点位置，然后拆成左右孩子
            for i in range(inStart, inEnd + 1):
                if inorder[i] == rootVal:
                    index = i
                    break
            # 构造根节点
            root = TreeNode(rootVal)
            leftLength = index - inStart
            # 递归生成左孩子
            root.left = build(preorder, preStart + 1, preStart + leftLength, inorder, inStart, index - 1)
            # 递归生成有孩子
            root.right = build(preorder, preStart + leftLength + 1, preEnd, inorder, index + 1, inEnd)
            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    # leetcode 106 从中序遍历和后续遍历构造二叉树
    def buildTree2(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        def build(inorder, inStart, inEnd, postorder, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None

            rootVal = postorder[postEnd]
            index = 0
            for i in range(inStart, inEnd+1):
                if inorder[i] == rootVal:
                    index = i
                    break
            root = TreeNode(rootVal)
            leftSize = index - inStart
            root.left = build(inorder, inStart, index-1, postorder, postStart, postStart+leftSize-1)
            root.right = build(inorder, index+1, inEnd, postorder, postStart+leftSize, postEnd-1)
            return root

        return build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

    # leetcode 652 寻找重复子树
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        memo = dict()
        res = []
        def traverse(root):
            # 递归先确定终止条件
            if root is None:
                return '#'

            left = traverse(root.left)
            right = traverse(root.right)

            subTree = left + ',' + right + ',' + str(root.val)

            freq = memo.get(subTree, 0)
            # 多次重复只加入一次
            if freq == 1:
                res.append(root)
            memo[subTree] = freq + 1
            return subTree
        traverse(root)
        return res




class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# leetcode 116 填充每个节点的下一个右侧节点指针
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_node(node1, node2):
            if node1 is None or node2 is None:
                return

            node1.next = node2
            connect_node(node1.left, node1.right)
            connect_node(node2.left, node2.right)
            connect_node(node1.right, node2.left)

        if root is None:
            return root
        connect_node(root.left, root.right)
        return root


