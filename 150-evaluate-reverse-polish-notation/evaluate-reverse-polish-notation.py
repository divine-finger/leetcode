class Solution(object):
    def evalRPN(self, tokens):
        s=[]
        d={"+":operator.add, "-":operator.sub,"*":operator.mul,"/":operator.truediv}
        for x in tokens:
            if x in d.keys():
                p=s.pop(len(s)-1)
                o=s.pop(len(s)-1)
                c=d[x](o,p)
                s.append(int(c))
            else:
                s.append(int(x))
        return int(s[0])
        """
        :type tokens: List[str]
        :rtype: int
        """
        