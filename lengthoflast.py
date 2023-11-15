class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag1 = False
        length = 0
        while True:
            for letter in s[::-1]:
                if letter != ' ' and not flag1:
                    flag1 = True
                if letter != ' ' and flag1:
                    length += 1
                if letter == ' ' and flag1:
                    return length
            return length

s = Solution()
print(s.lengthOfLastWord("a"))
