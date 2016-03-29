#!/usr/bin/python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

import math
import  sys   
sys.setrecursionlimit(1000000000)        

def isBadVersion(self, version):
    if version >= 1702766719: return True
    else: return False

class Solution():
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def SolutionIter(head, tail):
            # 用 xrange 代替 range 防止 memory error
            # range 会一次性生成所有数据，如果参数比较大，数据量可能有几GB，而 xrange 动态生成所需要的数据
            versions = xrange(head, tail + 1)
            mid = int(math.ceil(versions / 2.0)) - 1
            if isBadVersion(mid):
                if mid == 0:
                    return 1
                else:
                    return SolutionIter(head, versions[mid])
            else:
                if tail - versions[mid] == 1 or tail - versions[mid] == 0:
                    return tail
                else:
                    return SolutionIter(versions[mid], tail)
        return SolutionIter(1, n)

if __name__ == '__main__':
    sample = Solution()
    print sample.firstBadVersion(2126753390)
