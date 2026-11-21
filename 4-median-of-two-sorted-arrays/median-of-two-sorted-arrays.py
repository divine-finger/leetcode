class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        s = sorted(nums1 + nums2)
        n = len(s)
        return s[n // 2] if n % 2 == 1 else (s[n // 2 - 1] + s[n // 2]) / 2.0
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        