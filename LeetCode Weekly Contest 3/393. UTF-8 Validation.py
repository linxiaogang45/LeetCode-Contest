class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        t = len(data)
        i = 0
        try:
            while i<t:
                if data[i]>=248 or 128<=data[i]<192: return False
                elif data[i]<128: i+=1
                elif 192<=data[i]<224:
                    if data[i+1]<128 or data[i+1]>=192: return False
                    i+=2
                elif 224<=data[i]<240:
                    if data[i+1]<128 or data[i+1]>=192 or data[i+2]<128 or data[i+2]>=192: return False
                    i+=3
                elif 240<=data[i]<248:
                    if data[i+1]<128 or data[i+1]>=192 or data[i+2]<128 or data[i+2]>=192 or data[i+3]<128 or data[i+3]>=192: return False
                    i+=4
        except IndexError:
            return False
        return True

b = Solution()
print b.validUtf8([197, 130, 1])