"""234_Palindrome_Linked_List.py

Author: Juan Diego Becerra
Date:   06-10-2022
Brief:  https://leetcode.com/problems/palindrome-linked-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) | Space: O(1)
def isPalindrome(self, head: ListNode) -> bool:
    middle = middleNode(head)
    right = reverseList(middle)
    left = head

    while left and right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True


def middleNode(head: ListNode) -> ListNode:
    """Returns the middle node of a given linked list"""
    middle, dummy = head, head

    while dummy and dummy.next:
        middle = middle.next
        dummy = dummy.next.next

    return middle


def reverseList(head: ListNode) -> ListNode:
    """Reverses the nodes of a given linked list and returns head of the reversed list"""
    prev = None
    next_node = head

    while next_node:
        next_node = next_node.next
        head.next = prev
        prev = head
        head = next_node

    return prev
