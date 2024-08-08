# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
    
        while current or stack:
            while current:
                stack.append(current)  # 현재 노드를 스택에 추가하고 왼쪽으로 이동
                current = current.left
        
            current = stack.pop()  # 가장 왼쪽 노드를 꺼내서 방문
            result.append(current.val)  # 현재 노드 방문
            current = current.right  # 오른쪽 자식 노드로 이동
    
        return result

#https://leetcode.com/problems/binary-tree-inorder-traversal/