class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(filter(str.isalnum, s))
        new = new.lower()
        rev = new[::-1]
        return new==rev