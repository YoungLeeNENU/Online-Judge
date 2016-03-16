# -*- coding: utf-8 -*-
#!/usr/bin/python
# 此题可以不转成数字，直接从链表中取值逐位运算

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1, l2 = self.linkToList(l1), self.linkToList(l2)
        nil = ''
        rl1, rl2 = map(str, l1[::--1]), map(str, l2[::--1])
        n1, n2 = nil.join(rl1), nil.join(rl2)
        calced = str((int(n1[::-1])) + (int(n2[::-1])))[::-1]
        res = []
        for x in calced:
           res.append(int(x)) 
        return self.listToLink(res)
    def listToLink(self, list_instance):
        linkSeq = []
        for x in list_instance:
            tmpL = ListNode(x)
            linkSeq.append(tmpL)
        for i, x in enumerate(linkSeq):
            if i + 1 < len(linkSeq):
                x.next = linkSeq[i + 1]
            else:
                x.next = None
        return linkSeq[0]
    def linkToList(self, linked):
        con = [linked.val]
        while True:
            if linked.next is not None:
                con.append(linked.next.val)
                linked = linked.next
            else:
                break
        return con

if __name__ == '__main__':
    L10 = ListNode(2)
    L11 = ListNode(4)
    L12 = ListNode(3)
    L10.next = L11
    L11.next = L12

    L20 = ListNode(5)
    L21 = ListNode(6)
    L22 = ListNode(4)
    L20.next = L21
    L21.next = L22

    sample = Solution()
    result = sample.addTwoNumbers(L10, L20)
    print result.val
    print result.next
    print result.next.val
    print result.next.next
    print result.next.next.val
    print result.next.next.next
