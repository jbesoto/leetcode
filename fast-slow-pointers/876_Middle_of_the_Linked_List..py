"""876_Middle_of_the_Linked_List.py

Author: Juan Diego Becerra
Date:   06-13-2022
Brief:  https://leetcode.com/problems/middle-of-the-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) | Space: O(1)
def middleNode(self, head: ListNode) -> ListNode:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
