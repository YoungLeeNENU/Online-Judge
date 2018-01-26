# -*- coding: utf-8 -*-
#!/usr/bin/python

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = bin(n)[2:]
        return len(''.join(bin_str.split('0')))

if __name__ == '__main__':
    solution = Solution()
    print solution.hammingWeight(11)
