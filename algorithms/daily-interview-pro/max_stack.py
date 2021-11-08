class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.max_stack != []:
            if val >= self._maxtop():
                self.max_stack.append(val)
        else:
            self.max_stack.append(val)

    def pop(self) -> None:
        if self.top() == self._maxtop():
            self.max_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        if self.stack != []:
            return self.stack[-1]
        
    def _maxtop(self) -> int:
        if self.max_stack != []:
            return self.max_stack[-1]

    def max(self) -> int:
        return self._maxtop()


if __name__ == '__main__':
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    assert s.max() == 3
    # 3
    s.pop()
    s.pop()
    assert s.max() == 2
    # 2