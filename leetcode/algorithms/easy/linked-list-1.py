# -*- coding: utf-8 -*-
#!/usr/bin/python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

listNode1 = ListNode(1)
listNode2 = ListNode(2)
listNode3 = ListNode(3)
listNode4 = ListNode(4)
listNode1.next = listNode2
listNode2.next = listNode3
listNode3.next = listNode4

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':

    solution = Solution()
    # solution.deleteNode()        
