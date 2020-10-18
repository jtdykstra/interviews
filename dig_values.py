class Solution:
    def __init__(self):
        self.memo = {}

    def numDecodings(self, s):
        return self.numDecodingsHelper(s)
        
    def numDecodingsHelper(self, s: str) -> int:
        total = 0
        ways1 = 0
        ways2 = 0
        if (self.memo.get(s, False)):
            return self.memo[s]

        if (s != '' and s[0] == '0'):
            return 0
        if (s[1:] == ''):
            return 1
        
        
        ways1 = self.numDecodingsHelper(s[1:]) 
        self.memo[s[1:]] = ways1
        if (s[:2] != '' and int(s[:2]) <= 26):
            ways2 = self.numDecodingsHelper(s[2:])
            self.memo[s[2:]] = ways2

        return total + ways1 + ways2
# 226 -> 2 or 22
"""
22 6
2 26

"""
sol = Solution()
print(sol.numDecodings("226"))
print(sol.numDecodings("0"))
print(sol.numDecodings("27"))
