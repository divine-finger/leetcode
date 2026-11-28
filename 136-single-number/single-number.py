class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        from collections import Counter
        c=Counter(nums)
        l=[ k for k,v in c.items() if v==1]
        return l[0]