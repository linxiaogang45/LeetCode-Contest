class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n == 3: return 2
        if n%2 == 0:
            t = 1 + self.integerReplacement(n/2)
        else:
            if (n-1)%4 == 0:
                t = 2 + self.integerReplacement((n-1)/2)
            else:
                t = 2 + self.integerReplacement((n+1)/2)
        return t
b = Solution()
print b.integerReplacement(7)