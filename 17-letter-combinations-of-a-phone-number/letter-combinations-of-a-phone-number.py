class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        d = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        combinations = [""]
        for digit in digits:
            if digit in d:
                combinations = [
                    prefix + ch
                    for prefix in combinations
                    for ch in d[digit]
                ]

        return combinations
        """
        :type digits: str
        :rtype: List[str]
        """
        