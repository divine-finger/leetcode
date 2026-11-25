class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1]==9:
            s  =int("".join(map(str,digits))) +1 
            digits=[int(x) for x in str(s)]
        else:
            digits[-1]+=1
        return digits