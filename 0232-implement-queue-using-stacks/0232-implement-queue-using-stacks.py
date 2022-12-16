class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        if len(self.s)==0:
            self.s.append(x)
            return
        temp = self.s.pop(-1)
        self.push(x)
        self.s.append(temp)
        
    def pop(self) -> int:
        return self.s.pop(-1)

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()