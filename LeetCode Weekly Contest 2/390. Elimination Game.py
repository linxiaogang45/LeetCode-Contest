class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1 :
            return 1
        elif n == 2 or n == 3:
            return 2
        else:
            if n%4 ==0:
                return 4*self.lastRemaining(n/4)-2
            elif n%4 ==1:
                return 4*self.lastRemaining((n-1)/4)-2
            elif n%4 ==2:
                return 4 * self.lastRemaining((n - 2) / 4)
            else:
                return 4 * self.lastRemaining((n - 3) / 4)
b = Solution()
print b.lastRemaining(9)