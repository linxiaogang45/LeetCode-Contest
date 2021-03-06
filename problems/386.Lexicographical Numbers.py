'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        r = []
        if n<1: return r
        counter = 1
        i = 1
        state = 1
        while counter<=n and i<=n:
            if i==1 and state==2: break
            r.append(i)
            counter+=1
            while 10*i<=n:
                r.append(10*i)
                counter+=1
                i=10*i

            i+=1
            while i%10!=0 and i<=n:
                r.append(i)
                i+=1
                counter+=1
            if i>n: i=1+(n-n%10)/10
            while i%10==0:
                i=i/10
            if i==9: state=2

        return r


b = Solution()
print b.lexicalOrder(13)





The most elegant python solution from others:
    
    class Solution(object):
    def lexicalOrder(self, n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new /= 10
            ans.append(new)
        return ans
