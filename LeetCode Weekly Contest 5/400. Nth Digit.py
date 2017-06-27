import math
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        s = 0
        while True:
            a = n - 9*i*pow(10, i-1)
            if a==0:
                return 9
            elif a<0:
                break
            s += 9*pow(10, i-1)
            n = a
            i += 1
        if n%i == 0:
            t = (n/i)
            return int(list(str(s + t))[i-1])
        else:
            t = math.trunc(n/i)+1
            return int(list(str(s + t))[(n % i)-1])

b = Solution()
print b.findNthDigit(11)



