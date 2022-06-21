"""141_Linked_List_Cycle.py

Author: Juan Diego Becerra
Date:   06-13-2022
Brief:  https://leetcode.com/problems/linked-list-cycle/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(n) | Space O(1)
def hasCycle(head: ListNode) -> bool:
    if head:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

    return False


# =================================================================
# FLOYD'S HARE-TORTOISE ALGORITHM
# =================================================================
# If there is a cycle, slow and fast pointers will eventually meet
# at some node in the cycle.
#
# Proof: https://math.stackexchange.com/questions/913499/proof-of-floyd-cycle-chasing-tortoise-and-hare
