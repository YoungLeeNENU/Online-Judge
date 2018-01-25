# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
"""
import sys
sys.setrecursionlimit(1000000)            # 增加递归深度

class Solution(object):
    def __init__(self):
        self.palindromicCount = 0
    def  _isPalindromic(self, s):
        """
        :type s: str
        :rtype: int
        """
        return s[::-1] == s
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.str = s
        return self.str

if __name__ == '__main__':
    solution = Solution()
    testPackage = ["abc", "aaa"]
    for item in testPackage:
        print solution.countSubstrings(item)
