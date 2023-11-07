class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        o = []
        c = []
        if len(s) == 0 or len(s) == 1:
            return False
        for element in s:
            if element in d.keys():
                o.append(element)
            else:
                if len(o) == 0:
                    return False
                else:
                    if element != d[o.pop()]:
                        return False
        if len(o) != 0 or len(c) != 0:
            return False
        else:
            return True



s = Solution()
print(s.isValid("([)]"))
