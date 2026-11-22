class Solution(object):
    def myAtoi(self, s):
        g=''
        t=0
        p=True
        if 0<=len(s)<=200:
            for x in s.strip('_ '):
                if g=='' and x in '-+':
                    g+=x
                elif x.isdigit():
                    g+=x
                else:
                    break
            
            for y, x in enumerate(g):
                if y==0:
                    if x=='+':
                        p=True
                    elif x=='-':
                        p=False
                    else:
                        t+=int(x)*10**(len(g)-1-y)
                else:
                    t+=int(x)*10**(len(g)-1-y)
            if t.bit_length()>=32:
                if p:
                    return 2147483647
                return -2147483648
            else:
                if p:
                    return t
                return -t
        return 0

            


        """
        :type s: str
        :rtype: int
        """
        