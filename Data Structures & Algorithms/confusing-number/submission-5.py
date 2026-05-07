class Solution:
    def confusingNumber(self, n: int) -> bool:

        n = str(n)

        new_n = ""

        for i in n:
            if i in ["2", "3", "4", "5", "7"]:
                return False
            if i in ["0", "1", "8"]:
                new_n = i + new_n
            if i == "6":
                new_n = "9" + new_n
            if i == "9":
                new_n = "6" + new_n

        return n != new_n
