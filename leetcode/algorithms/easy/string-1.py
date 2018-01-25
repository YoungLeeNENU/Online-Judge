# -*- coding: utf-8 -*-
#!/usr/bin/python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        import math
        mid_index = int(math.ceil(len(s) / 2.0)) - 1
        list_s = list(s)
        for i, x in enumerate(list_s):
            if i <= mid_index:
                tmp = list_s[i]
                list_s[i] = list_s[len(list_s) - 1 - i]
                list_s[len(list_s) - 1 - i] = tmp
        return "".join(list_s)
    
if __name__ == '__main__':
    solution = Solution()
    print solution.reverseString("younglee")
