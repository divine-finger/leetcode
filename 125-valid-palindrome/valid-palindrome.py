class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        s=s.lower()
        c="".join(x for x in s if x.isalnum())
        return c==c[::-1]