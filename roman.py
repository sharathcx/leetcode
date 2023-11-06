class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = 0
        for i in range(len(s) - 1):
            if s[i + 1] in "VXLCDM":
                if d[s[i + 1]] > d[s[i]]:
                    n -= d[s[i]]
                else:
                    n += d[s[i]]
            else:
                n += d[s[i]]
        n += d[s[-1]]
        return n

s1 = Solution()
print(s1.romanToInt("XCIX"))
