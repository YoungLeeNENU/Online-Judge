# -*- coding: utf-8 -*-
#!/usr/bin/python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
root.left = node1
root.right = node2
node2.right = node3
node3.right = node4

class Solution(object):
    def __init__(self):
        self.tree_depth = 1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepthIteration(root, depth):
            if depth > self.tree_depth:
                self.tree_depth = depth
            if root.left != None:
                maxDepthIteration(root.left, depth + 1)
            if root.right != None:
                maxDepthIteration(root.right, depth + 1)
        maxDepthIteration(root, self.tree_depth)
        return self.tree_depth

if __name__ == '__main__':
    solution = Solution()
    print solution.maxDepth(root)
