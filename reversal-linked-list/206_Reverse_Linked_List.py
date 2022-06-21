"""206_Reverse_Linked_List.py

Author: Juan Diego Becerra
Date:   06-10-2022
Brief:  https://leetcode.com/problems/reverse-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) | Space: O(1)
def reverseList(head: ListNode) -> ListNode:
    prev = None
    next_node = head

    while next_node:
        next_node = next_node.next
        head.next = prev
        prev = head
        head = next_node

    return prev
