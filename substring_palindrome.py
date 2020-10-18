class Solution:
    def __init__(self):
        self.repeated = {}
    
    def longestPalindrome(self, s: str) -> str:
        self.repeated.clear()
        return self.longestPalindromeHelper(s)

        
    def longestPalindromeHelper(self, s: str) -> str:
        # base cases
        if (len(s) == 1):
            return s
        if (len(s) <= 0):
            return ''

        # this substring has been checked already
        if (self.repeated.get(s, False) != False):
            return self.repeated.get(s, False) 

        # if it's a palindrome, no  need to go further
        if (s == s[::-1]):
            return s

        left = self.longestPalindromeHelper(s[1:])
        right = self.longestPalindromeHelper(s[:-1])
        longest = left if len(left) > len(right) else right 
        self.repeated[s] = longest 
        return longest 

sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome('a'))
print(sol.longestPalindrome('ac'))
print(sol.longestPalindromeHelper("abbcccbbbcaaccbababcbcabca"))
print(sol.longestPalindromeHelper("miycvxmqggnmmcwlmizfojwrurwhwygwfykyefxbgveixykdebenzitqnciigfjgrzzbtgeazyrbiirmejhdwcgjzwqolrturjlqpsgunuqerqjevbheblmbvgxyedxshswsokbhzapfuojgyfhctlaifrisgzqlczageirnukgnmnbwogknyyuynwsuwbumdmoqwxprykmazghcpmkdcjduepjmjdxrhvixxbfvhybjdpvwjbarmbqypsylgtzyuiqkexgvirzylydrhrmuwpmfkvqllqvekyojoacvyrzjevaupypfrdguhukzuqojolvycgpjaendfetkgtojepelhcltorueawwjpltehbbjrvznxhahtuaeuairvuklctuhcyzomwrrznrcqmovanxmiyilefybkbveesrxkmqrqkowyrimuejqtikcjfhizsmumajbqglxrvevexnleflocxoqgoyrzgqflwiknntdcykuvdcpzlakljidclhkllftxpinpvbngtexngdtntunzgahuvfnqjedcafzouopiixw"))

