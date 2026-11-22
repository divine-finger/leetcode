class Solution(object):
    def romanToInt(self, s):
        v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        indi = {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
        re = t = 0
        st = 1
        if len(s) == 1:
            return v[s]

        for y, x in enumerate(s):
            # skipping one
            if t and y == t:
                t = 0
                continue

            if y < len(s) - 1:
                c = s[y + 1]

                # 9 4 thing
                if x in 'IXC' and (indi[c] - indi[x] == 2 or indi[c] - indi[x] == 1):
                    re += v[c] - v[x]
                    t = y + 1

                # same digit
                elif indi[x] == indi[c]:
                    st += 1
                else:
                    re += st * v[x]
                    st = 1
            else:
                re += st * v[x]
                st = 1

        return re