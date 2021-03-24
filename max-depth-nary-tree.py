# Link to Leetcode problem: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Difficulty: Easy

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if root is None:
            return 0
        elif root.children is None:
            return 1
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1