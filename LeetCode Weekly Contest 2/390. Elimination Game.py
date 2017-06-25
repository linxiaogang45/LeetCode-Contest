'''There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9

Output:
6
'''





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
