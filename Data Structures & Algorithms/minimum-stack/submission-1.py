class MinStack:

    def __init__(self):
        self.s = []
        self.store = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.store:
            self.store.append(min(val, self.store[-1]))
        else:
            self.store.append(val)
        
        
    def pop(self) -> None:
        self.s.pop()
        self.store.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.store[-1]
