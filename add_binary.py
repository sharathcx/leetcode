class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:
            for i in range(len_a - len_b):
                b = "0" + b
        else:
            for i in range(len_b - len_a):
                a = "0" + a
        carry = "0"
        for i in range(len(a), 0, -1):
            k = i
            bin1 = a[i - 1]
            bin2 = b[i - 1]
            if carry == "0":
                if bin1 == "0":
                    sum = bin2 + sum
                else:
                    if bin2 == "0":
                        sum = bin1 + sum
                    else:
                        sum = "0" + sum
                        carry = "1"
            else:
                if bin1 == "0":
                    if bin2 == "0":
                        sum = "1" + sum
                        carry = "0"
                    else:
                        sum = "0" + sum
                        carry = "1"
                else:
                    if bin2 == "0":
                        sum = "0" + sum
                        carry = "1"
                    else:
                        sum = "1" + sum
                        carry = "1"
        if carry == "1":
            sum = "1" + sum
        return sum


s = Solution()
print(s.addBinary(a="1", b="111"))
