class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(len(s)):
            # Check odd-length palindromes (e.g., "bab")
            odd = expand(i, i)
            # Check even-length palindromes (e.g., "bb")
            even = expand(i, i + 1)
            
            res = max(res, odd, even, key=len)
            
        return res
        """
        :type s: str
        :rtype: str
        """
        