class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        student_count = Counter(students)

        for s in sandwiches:
            if student_count[s] == 0:
                return student_count[0] + student_count[1]
            else:
                student_count[s] -= 1

        return 0
