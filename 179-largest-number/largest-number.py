class Solution(object):
    def largestNumber(self, nums):
        re = ''
        s = sorted(nums, key=lambda x: (tuple(int(str(x)[c]) for c in range(len(str(x)))) + (-len(str(x)),)))
        s = s[::-1]
        for y, x in enumerate(s):
            c = y
            while c > 0 and str(s[c - 1]) + str(s[c]) < str(s[c]) + str(s[c - 1]):
                s[c - 1], s[c] = s[c], s[c - 1]
                c -= 1
        for x in s:
            re += str(x)
        return "0" if re and re[0] == '0' else re
        """
        :type nums: List[int]
        :rtype: str
        """
        