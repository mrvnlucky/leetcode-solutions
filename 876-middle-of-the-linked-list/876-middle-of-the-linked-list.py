# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # check if fast node is still on the linked list
        # and check if it is on the end of the lsit
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow