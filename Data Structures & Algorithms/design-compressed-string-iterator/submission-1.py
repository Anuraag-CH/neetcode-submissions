class StringIterator:
    def __init__(self, compressedString: str):
        self.arr = []
        s = ""
        for c in compressedString:
            if c.isalpha():
                if s:
                    self.arr.append(int(s))
                    s = ""

                self.arr.append(c)
            else:
                s += c

        self.arr.append(int(s))

        self.i = 0

    def next(self) -> str:

        ele = self.arr[self.i]

        self.arr[self.i + 1] -= 1

        if self.arr[self.i + 1] == 0:
            self.i += 2

        return ele

    def hasNext(self) -> bool:

        return True if self.i < len(self.arr) else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
