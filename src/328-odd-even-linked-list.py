'''https://leetcode.com/problems/odd-even-linked-list/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Maintaining two pointers for odd and even 
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr = head
        i = 1
        odd = o = ListNode(0)
        even = e = ListNode(0)
        while curr:
            # print(i, o, e)
            if i%2==0:  #even
                e.next = curr
                curr = curr.next
                e.next.next = None
                e = e.next
            else:
                o.next = curr
                curr = curr.next
                o.next.next = None
                o = o.next
            i+=1
            
        o.next = even.next
        return odd.next