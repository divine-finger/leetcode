class Solution:
    def canAliceWin(self, n: int) -> bool:
        a=10
        c=0
        if n<10:
            return False
        while n>=0:
            n-=a
            c+=1
            a-=1
        return c%2==0