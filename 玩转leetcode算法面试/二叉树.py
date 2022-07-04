# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 104二叉树的最大深度
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return max(left_max, right_max) + 1

    # 111二叉树的最小深度
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is not None and root.right is not None:
            leftMin = self.minDepth(root.left)
            rightMin = self.minDepth(root.right)
            return min(leftMin, rightMin) + 1
        else:
            leftMin = self.minDepth(root.left)
            rightMin = self.minDepth(root.right)
            return max(leftMin, rightMin) + 1

    # 226翻转二叉树
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    # 100相同的树
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None
        if q is None:
            return p is None
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 101对称二叉树
    def isSymmetric(self, root) -> bool:
        def isSymmetricHelp(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return isSymmetricHelp(left.left, right.right) and isSymmetricHelp(left.right, right.left)
        return root is None or isSymmetricHelp(root.left, root.right)

    # 222完全二叉树的节点个数
    def countNodes(self, root: TreeNode) -> int:
        l, r = root, root
        lh, rh = 0, 0
        while l is not None:
            l = l.left
            lh += 1
        while r is not None:
            r = r.right
            rh += 1
        if lh == rh:
            return pow(2, lh) - 1
        # 此时l和r已经是None了
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # 110平衡二叉树
    def isBalanced(self, root: TreeNode) -> bool:
        def max_depth(root):
            if root is None:
                return 0
            left_max_depth = max_depth(root.left)
            right_max_depth = max_depth(root.right)
            return max(left_max_depth, right_max_depth) + 1
        if root is None:
            return True
        l_depth = max_depth(root.left)
        r_depth = max_depth(root.right)
        if abs(l_depth-r_depth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    # 404左叶子之和
    def sumOfLeftLeaves(self, root) -> int:
        if root is None:
            return 0
        sum = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            sum += root.left.val
        sum += self.sumOfLeftLeaves(root.left)
        sum += self.sumOfLeftLeaves(root.right)
        return sum

    # 257二叉树的所有路径
    def binaryTreePaths(self, root) -> list[str]:
        res = []
        if root is None:
            return res
        if root.left is None and root.right is None:
            res.append(str(root.val))
            return res
        leftP = self.binaryTreePaths(root.left)
        for i in range(len(leftP)):
            res.append(str(root.val)+'->'+leftP[i])
        rightP = self.binaryTreePaths(root.right)
        for i in range(len(rightP)):
            res.append(str(root.val)+'->'+rightP[i])
        return res

    # 113路径总和II
    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        def find(root, sum, path):
            if root is None:
                return
            path.append(root.val)
            if root.left is None and root.right is None and root.val==sum:
                res.append(path[:])
                #return 早退报错了
            find(root.left, sum-root.val, path)
            find(root.right, sum-root.val, path)
            path.pop()

        res = []
        path = []
        find(root, targetSum, path)
        return res

    # 437路径总和III
    def pathSum(self, root, targetSum: int) -> int:
        def find(root, sum):
            if root is None:
                return 0
            res = 0
            if root.val == sum:
                res += 1
            res += find(root.left, sum - root.val)
            res += find(root.right, sum - root.val)
            return res

        if root is None:
            return 0
        res = find(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res

    # 235二叉搜索树的最近公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # 236二叉树的最近公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p is None or q is None:
            return None
        if root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l if l else r

    # 98验证二叉搜索树
    def isValidBST(self, root) -> bool:
        def isBST(root, MIN, MAX):
            if root is None:
                return True
            if root.val <= MIN or root.val >= MAX:
                return False
            return isBST(root.left, MIN, root.val) and isBST(root.right, root.val, MAX)

        MIN = -float('inf')
        MAX = float('inf')
        return isBST(root, MIN, MAX)

    # 108将有序数组转换为二叉搜索树
    def sortedArrayToBST(self, nums: list[int]) -> 'TreeNode':
        def insert(nums, low, high, root):
            if low <= high:
                mid = (high+low) // 2
                if root is None:
                    root = TreeNode(nums[mid])
                root.left = insert(nums, low, mid-1, root.left)
                root.right = insert(nums, mid+1, high, root.right)
            return root

        low = 0
        high = len(nums) - 1
        return insert(nums, low, high, None)
