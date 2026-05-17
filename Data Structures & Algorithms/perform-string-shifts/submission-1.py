class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        left_shift = 0
        right_shift = 0

        s = [i for i in s]

        for sh in shift:
            if sh[0] == 0:
                left_shift += sh[1]
            else:
                right_shift += sh[1]

        right_shift -= left_shift

        if right_shift > 0:
            while right_shift > 0:
                ele = s.pop()
                s.insert(0, ele)
                right_shift -= 1

        else:
            left_shift = abs(right_shift)
            while left_shift > 0:
                ele = s.pop(0)
                s.append(ele)
                left_shift -= 1

        return "".join(s)
