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