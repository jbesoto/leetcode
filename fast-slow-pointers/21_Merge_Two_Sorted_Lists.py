"""21_Merge_Two_Sorted_Lists.py

Author: Juan Diego Becerra
Date:   06-14-2022
Brief:  https://leetcode.com/problems/merge-two-sorted-lists/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n) | Space: O(n)
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    merged = ListNode()
    curr = merged

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return merged.next
