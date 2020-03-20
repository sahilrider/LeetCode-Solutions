'''https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def bfs(self, root):
        q = [(root, 0)]
        prevNode, prevStep = None, None
        while q:
            node, step = q.pop(0)
            if node:
                if node.left: q.append((node.left, step+1))
                if node.right: q.append((node.right, step+1))
            if prevNode:
                if prevStep==step:
                    prevNode.next = node
            prevNode, prevStep = node, step
        return root
    
    def connect(self, root: 'Node') -> 'Node':
        return self.bfs(root)
        