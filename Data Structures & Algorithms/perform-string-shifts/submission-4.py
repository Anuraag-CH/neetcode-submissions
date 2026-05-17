class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        left_shift = 0
        right_shift = 0

        for sh in shift:
            if sh[0] == 0:
                left_shift += sh[1]
            else:
                right_shift += sh[1]

        if left_shift > right_shift:
            left_shift -= right_shift

            left_shift = left_shift % len(s)

            s = s[left_shift:] + s[:left_shift]

        else:
            right_shift -= left_shift
            right_shift = right_shift % len(s)
            s = s[-right_shift:] + s[:-right_shift]

        return s
