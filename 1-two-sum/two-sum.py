class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen_numbers = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen_numbers:
                return seen_numbers[needed],i
            seen_numbers[num] = i

        return None