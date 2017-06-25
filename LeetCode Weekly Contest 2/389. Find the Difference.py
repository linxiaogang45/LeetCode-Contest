from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            r = t
            t = s
            s = r
        a = dict(Counter(s))
        b = dict(Counter(t))
        try:
            for i in a:
                if a[i] != b[i]:
                    return i
                    break
        except KeyError:
            return i

b = Solution()
print b.findTheDifference("abcd","abcde")