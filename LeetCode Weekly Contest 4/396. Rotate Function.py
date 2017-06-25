class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        a = []
        t, s = 0, 0
        for i in range(n):
          t += i*A[i]
          s += A[i]
        a.append(t)
        for k in range(1, n):
          t = a[k-1] + s - n*A[n-k]
          a.append(t)
        return max(a)
b = Solution()
print b.maxRotateFunction([4, 3, 2, 6])