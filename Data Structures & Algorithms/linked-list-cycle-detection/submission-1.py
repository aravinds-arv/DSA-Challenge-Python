# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        p1, p2 = head, head.next
        flag = False

        while p2:
            if p2 == p1:
                return True

            if flag:
                p1 = p1.next
            
            p2 = p2.next
            flag = not flag
        
        return False