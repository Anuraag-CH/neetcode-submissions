class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self._sum = 0
        self.cur_size = 0

    def next(self, val: int) -> float:

        if self.cur_size < self.size:
            self.cur_size += 1

        else:
            ele = self.queue.popleft()
            self._sum -= ele

        self.queue.append(val)
        self._sum += val
        return self._sum / self.cur_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
