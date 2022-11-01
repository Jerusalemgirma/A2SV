class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min_vals = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        if self.min_vals:
            self.min_vals.append(min(self.min_vals[-1], x))
        else:
            self.min_vals.append(x)

    def pop(self) -> None:
        if self.nums:
            self.nums.pop()
            self.min_vals.pop()

    def top(self) -> int:
        if self.nums:
            return self.nums[-1]

    def getMin(self) -> int:
        if self.nums:
            return self.min_vals[-1]