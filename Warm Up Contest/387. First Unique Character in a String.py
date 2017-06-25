'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = s
        while len(r) != 0:
            x = r[0]
            t = r.replace(x, '')
            if len(t) == len(r)-1: break
            r = t
        if len(r) != 0:
            return s.find(x)
        else:
            return -1

b = Solution()
print b.firstUniqChar("loveleetcode")
