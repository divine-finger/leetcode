class Solution:
    def addDigits(self, num: int) -> int:
        c=0
        while num//10!=0:
            for x in str(num):
                c+=int(x)
            num=c
            c=0
        return num