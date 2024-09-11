from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False

        leaf_node_list1 = []
        leaf_node_list2 = []

        self.traverse_root(leaf_node_list1, root1)
        self.traverse_root(leaf_node_list2, root2)
    
        print(leaf_node_list1)
        print(leaf_node_list2)
        return leaf_node_list1 == leaf_node_list2
        
    def traverse_root(self, leaf_node_list: list, root: Optional[TreeNode]):
        def traverse(node: Optional[TreeNode]):
            if node.left:
                traverse(node.left)
            
            if node.right:
                traverse(node.right)
            
            if not node.left and not node.right:
                leaf_node_list.append(node.val)
        
        traverse(root)
