'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''



class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)
        if len(num)==k: return '0'
        try:
            while k > 0:
                while num[0] == '0':
                    num.remove(num[0])
                i = 0
                Der = 0
                while i <= len(num) - 2 and Der == 0:
                    if num[i] > num[i + 1]:
                        Der = 1
                        num.remove(num[i])
                    i += 1
                if Der == 0: num.pop()
                k -= 1
            while num[0] == '0':
                num.remove(num[0])
            s = ''
            for i in range(len(num)):
                s += num[i]
            return s
        except IndexError:
            return '0'

b = Solution()
print b.removeKdigits("112", 1)




