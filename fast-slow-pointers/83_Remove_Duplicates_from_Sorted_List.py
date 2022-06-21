"""83_Remove_Duplicates_from_Sorted_List.py

Author: Juan Diego Becerra
Date:   06-14-2022
Brief:  https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) | Space: O(1)
def deleteDuplicates1(head: ListNode) -> ListNode:
    curr = head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next

    return head


# Time: O(n) | Space: O(n)
def deleteDuplicates2(head: ListNode) -> ListNode:
    seen = set()
    curr, prev = head, head

    while curr:
        if curr.val in seen:
            dummy = curr
            curr = curr.next
            dummy.next = None
            prev.next = curr

        else:
            seen.add(curr.val)
            prev = curr
            curr = curr.next

    return head
