# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        
        # Let's divide this problem into 3 parts
        # PART 1: Find the middle node

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # here slow is in the middle
        second = slow.next
        slow.next = None # This breaks the list in half
        # now we reverse the half list
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Now we have to merge the list
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
    


