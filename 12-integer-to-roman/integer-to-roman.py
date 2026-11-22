class Solution(object):
    def intToRoman(self, num):
        l=[]
        p=[]
        re=''
        d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        if 1<=num<=3999:
            for y,x in enumerate(str(num)):
                diff=10**(len(str(num))-1-y)
                l.append(int(x)*diff)
                p.append(diff)
            for x,y in list(zip(l,p)):
                c=x//y
                if 0<c<4:
                    re+=c*d[y]
                elif c==4 :
                    re+=d[y]+d[y*5]
                elif c==9:
                    re+=d[y]+d[y*10]
                elif c==5:
                    re+=d[y*5]
                elif 5<c<9:
                    re+=d[y*5]+(c-5)*d[y]
            return re
        return 0

        """
        :type num: int
        :rtype: str
        """
        