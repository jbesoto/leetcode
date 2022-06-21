"""203_Remove_Linked-List_Elements.py

Author: Juan Diego Becerra
Date:   06-10-2022
Brief:  https://leetcode.com/problems/remove-linked-list-elements/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) | Space: O(1)
def removeElements(head: ListNode, val: int) -> ListNode:
    curr, next_node = head, head
    prev = None
    while next_node:
        next_node = next_node.next

        if curr.val == val:
            curr.next = None
            curr = next_node

            if not prev:
                head = curr
            else:
                prev.next = curr

        else:
            prev = curr
            curr = next_node

    return head
