class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_index = 0
        common_str = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            minimum = len(strs[0])
            for i in range(len(strs) - 1):
                l = len(strs[i])
                s = strs[i]
                if minimum > len(strs[i + 1]):
                    minimum = len(strs[i+1])
                    min_index = i + 1
            if minimum == 0:
                return ""

            for i, letter in enumerate(strs[min_index]):
                flag = True
                for j in range(len(strs)):
                    if strs[j][i] != letter:
                        flag = False
                if flag:
                    # if letter not in common_str:
                    common_str += letter
                else:
                    return common_str
            return common_str



