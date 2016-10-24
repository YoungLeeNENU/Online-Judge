# -*- coding: utf-8 -*-
#!/usr/bin/python
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.substr = ""
        self.substr_pool = []
    def traversal(self, root):
        if self.left == self.right == None:
            root.substr = root.substr + self.val
            root.substr_pool.append(root.substr)
            root.substr = ""
            return
        elif self.left == None and self.right != None:
            root.substr = root.substr + self.val
            root.substr_pool.append(root.substr)
            root.substr = ""
            return self.right.traversal(root)
        elif self.left != None and self.right == None:
            root.substr = root.substr + self.val
            return self.left.traversal(root)
        else:
            return

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash_table = []
        tmp = ""
        for i, x in enumerate(s):
            for j, y in enumerate(s[i:]):
                try:
                    tmp.index(y)
                    print s[i:]
                    if tmp not in hash_table:
                        hash_table.append(tmp)
                    tmp = ""
                    break
                except ValueError:
                    tmp += y
                    if j + 1 == len(s[i:]) and tmp not in hash_table:
                        hash_table.append(tmp)
                        tmp = ""
                        break
        len_table = map(lambda x: len(x), hash_table)
        return max(len_table) if len_table != [] else 0
    def _lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        root = TreeNode("")    # initial
        history = None
        for x in s:
            if history == None:
                new_node = TreeNode(x)
                root.left = new_node
                history = new_node
            else:
                new_node = TreeNode(x)
                if history.val == x:
                    history.right = new_node
                    history = new_node
                else:
                    history.left = new_node
                    history = new_node
        root.traversal(root)
        return max(map(len, root.substr_pool))

if __name__ == '__main__':
    sample = Solution()
    print sample.lengthOfLongestSubstring("abcabcbb")
    # print sample.lengthOfLongestSubstring(big_txt)
    
