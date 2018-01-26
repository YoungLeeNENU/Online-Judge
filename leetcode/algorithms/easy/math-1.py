# -*- coding: utf-8 -*-
#!/usr/bin/python

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i, x in enumerate(n * "1"):
            fizzBuzz = ""
            if (i + 1) % 3 == 0: fizzBuzz += "Fizz"
            if (i + 1) % 5 == 0: fizzBuzz += "Buzz"
            if len(fizzBuzz) > 0: result.append(fizzBuzz)
            else: result.append(str(i + 1))
        return result

if __name__ == '__main__':
    solution = Solution()
    print solution.fizzBuzz(16)
