'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''


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



