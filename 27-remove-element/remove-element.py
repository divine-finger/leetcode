class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l=nums.copy()
        for x in nums:
            if x==val:
                l.remove(x)
        nums[:len(nums)]=l
        return len(l)
        