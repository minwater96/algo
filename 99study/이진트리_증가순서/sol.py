Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        nodes = []
        inorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None

        return nodes[0]

# Helper function to print the tree in-order (for testing purposes)
    def print_inorder(root):
        if not root:
            return
        print_inorder(root.left)
        print(root.val, end=' -> ')
        print_inorder(root.right)    

#https://leetcode.com/problems/increasing-order-search-tree/