class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, l1 in enumerate(needle):
            for j, l2 in enumerate(haystack):
                if l1 == l2:
                    # s = haystack[j:len(needle) + j]
                    if haystack[j:len(needle) + j] == needle:
                        return j
        return -1


s = Solution()
s.strStr("hello", "ll")
