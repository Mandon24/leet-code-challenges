from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My recursion solution
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        tree = []
        found_node = None
        def traverse(node: TreeNode):
            nonlocal found_node
            if node.val == val:
                found_node = node

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)


        traverse(root)

        if not found_node:
            return None

        return found_node


# While loop solution
# Definition for a binary tree node.
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         current = root
#         while current:
#             if val == current.val:
#                 return current
#             elif val < current.val:
#                 current = current.left
#             else:
#                 current = current.right
#         return None
