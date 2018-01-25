# -*- coding: utf-8 -*-
#!/usr/bin/python

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_len = 0
        for index, element in enumerate(nums):
            if index != len(nums) - 1:
                if element == nums[index + 1]: pass
                else: set_len += 1
            else: set_len += 1
        return set_len
        
if __name__ == '__main__':
    solution = Solution()
    print solution.removeDuplicates([1, 1, 2])
