'''https://leetcode.com/problems/add-two-numbers/'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        temp = res
        c = 0
        while(l1!=None and l2!=None):
            val = l1.val+l2.val+c
            l1 = l1.next
            l2 = l2.next
            if val<10:
                t = ListNode(val)
                c = 0
            else:
                t = ListNode(val-10)
                c = 1
            temp.next = t
            temp = temp.next
        while l1 is not None:
            val = l1.val+c
            l1 = l1.next
            if val<10:
                t = ListNode(val)
                c = 0
            else:
                t = ListNode(val-10)
                c = 1
            temp.next = t
            temp = temp.next
        while l2 is not None:
            val = l2.val+c
            l2 = l2.next
            if val<10:
                t = ListNode(val)
                c = 0
            else:
                t = ListNode(val-10)
                c = 1
            temp.next = t
            temp = temp.next
        if c==1:
            temp.next = ListNode(1)
        return res.next
        