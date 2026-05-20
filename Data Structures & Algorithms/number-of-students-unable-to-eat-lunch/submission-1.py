class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        from collections import Counter, deque

        students_counter = Counter(students)
        students_queue = deque()
        sandwiches_queue = deque()

        # for i in students:
        students_queue.extend(students)
        sandwiches_queue.extend(sandwiches)

        while students_queue:
            if students_counter[0] == 0:
                del students_counter[0]
            if students_counter[1] == 0:
                del students_counter[1]

            if len(students_counter) == 1:
                if students_queue[0] != sandwiches_queue[0]:
                    return len(students_queue)

            if students_queue[0] == sandwiches_queue[0]:
                students_counter[sandwiches_queue[0]] -= 1
                students_queue.popleft()
                sandwiches_queue.popleft()
            else:
                ele = students_queue.popleft()
                students_queue.append(ele)

        return 0
