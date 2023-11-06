class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_str = ""
        minimum = 1
        for i in range(len(strs) - 1):
            minimum = len(strs[i])
            if minimum > len(strs[i + 1]):
                minimum = len(strs[i + 1])

        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                s1 = strs[i][:minimum]
                s2 = strs[j][:minimum]
                if strs[i][:minimum] != strs[j][:minimum]:
                    flag = False
            if flag:
                return strs[i][:minimum]
            else:
                minimum -= 1
        return ""


s = Solution()
print(s.longestCommonPrefix(["cir", "car"]))
