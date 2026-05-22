class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = []

        for i in range(0, len(num) - 2):
            digit = num[i : i + 3]

            val = digit[0]

            same = True
            for i in digit:
                if i != val:
                    same = False
                    break

            if same:
                res.append(int(digit))

        if not res:
            return ""

        res_val = max(res)
        return "000" if res_val == 0 else str(max(res))
