# -*- coding: utf-8 -*-
#!/usr/bin/python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            index = i
            seeking_half = target - x
            try:
                seeking_index = nums.index(seeking_half)
                if seeking_index != index:
                    return [index, seeking_index]
                else: 
                    continue
            except ValueError: 
                continue

if __name__ == '__main__':
    sample = Solution()
    print sample.twoSum([3, 2, 4], 6)
