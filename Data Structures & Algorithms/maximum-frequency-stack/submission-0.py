class FreqStack:

    def __init__(self):
        self.freq = {}
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        
        freq = self.freq[val] + 1
        self.freq[val] = freq

        self.maxCount = max(freq, self.maxCount)

        if freq not in self.stacks:
            self.stacks[freq] = []
        self.stacks[freq].append(val)

    def pop(self) -> int:
        v = self.stacks[self.maxCount].pop()
        self.freq[v] -= 1

        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return v
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()