'''https://leetcode.com/problems/serialize-and-deserialize-binary-tree/'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
            else:
                res.append(None)
            if node:
                q.extend([node.left, node.right])
        # print(res)
        return res
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        root = TreeNode(data.pop(0))
        q = [root]
        while q:
            node = q.pop(0)
            if node.val is not None:
                # print(node.val, data)
                left = data.pop(0)
                right = data.pop(0)
                if left is not None:
                    node.left = TreeNode(left)
                    q.append(node.left)
                if right is not None:
                    node.right = TreeNode(right)
                    q.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))