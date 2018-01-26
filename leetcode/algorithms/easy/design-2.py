# -*- coding: utf-8 -*-
#!/usr/bin/python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.internal_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.internal_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.internal_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.internal_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        min = self.internal_stack[0]
        for x in self.internal_stack:
            if x < min:
                min = x
        return min

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(1)
    minStack.push(4)
    minStack.push(7)
    minStack.push(0)
    print minStack.getMin()
