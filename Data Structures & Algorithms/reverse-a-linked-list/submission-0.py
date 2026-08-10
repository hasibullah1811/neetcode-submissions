# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 -> 1 -> 2 -> 3
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
