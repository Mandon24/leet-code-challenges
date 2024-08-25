from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_node = temp_node = ListNode()
        current_node = head
        list_prev_nodes = []
        
        while current_node:
            list_prev_nodes.insert(0, current_node.val)
            current_node = current_node.next
        
        for i in range(0, len(list_prev_nodes)):
            temp_node.next = ListNode(list_prev_nodes[i])
            temp_node = temp_node.next
    
        return reversed_node.next
