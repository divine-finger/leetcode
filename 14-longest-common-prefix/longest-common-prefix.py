class Solution(object):
    def longestCommonPrefix(self, strs):
        re=''
        s=strs[0]
        for x in strs:
            if x==s:
                continue
            for x,y in enumerate(x):
                if x<len(s):
                    if y == s[x]:
                        re+=y
                    else:
                        break
            s,re=re,''

        return s
            
        """
        :type strs: List[str]
        :rtype: str
        """
        