class Solution(object):
    def isValid(self, s):
        p = {"(": ")", "{": "}", "[": "]"}
        l = []
        for x in s:
            if x in p:
                l.append(p[x])
            else:
                if not l or l.pop() != x:
                    return False
        return len(l) == 0