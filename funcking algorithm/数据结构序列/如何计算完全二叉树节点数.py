# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class Solution(object):
    def countNodes(self, root):
        l = r = root
        hl = hr = 0

        while l is not None:
            l = l.left
            hl += 1
        while r is not None:
            r = r.right
            hr += 1

        if hl == hr:
            return pow(2, hl) - 1

        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)