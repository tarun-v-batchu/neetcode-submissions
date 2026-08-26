class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []


    def push(self, val: int) -> None:
        self.stack += [val]
        self.mini += [val if self.mini == [] else min(val, self.mini[-1])]
        

    def pop(self) -> None:
        if self.stack :
            self.stack.pop()
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]
