class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = 0
        n = 0
        while n<len(s):
            while m<len(t):
                if t[m]==s[n]:
                    break
                m+=1
            if m==len(t):
                break
            n+=1
            m+=1
        if n==len(s):
            return True
        else:
            return False

b = Solution()
print b.isSubsequence("axc", "ahbgdc")