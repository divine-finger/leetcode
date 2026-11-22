class Solution(object):
    def reverse(self, x):
        g=int(str(abs(x))[::-1])
        if g.bit_length()<32:
            if x>0:
                return g
            else:
                return -g
        return 0
        """
        :type x: int
        :rtype: int
        """
        