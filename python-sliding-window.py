class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == ''):
            return 0

        h = {}
        m = float('-inf')
        i = 0
        j = 0
        
        while (i < len(s) and j < len(s)):
            if (not h.get(s[j], False)):
                h[s[j]] = True
                j += 1
                if (j - i > m):
                    m = j - i
            else:
                h[s[i]] = False
                i += 1
        return m

sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcabc'))
print(sol.lengthOfLongestSubstring('dvdf'))


        
        