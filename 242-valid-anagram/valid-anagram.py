class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=[0]*26
        if len(s)!=len(t):
            return False
        for x in s:
            c[ord(x)-ord("a")] +=1
        for x in t:
            c[ord(x)-ord('a')]-=1
        return all(x==0 for x in c)