class Solution(object):
    def removeDuplicates(self, nums):
        l=list(set(nums))
        l.sort()
        nums[:len(l)]=l
        return len(l)
        """
        :type nums: List[int]
        :rtype: int
        """
        