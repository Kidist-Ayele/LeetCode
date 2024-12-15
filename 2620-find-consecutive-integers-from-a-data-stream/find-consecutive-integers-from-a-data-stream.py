class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.length = 0
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.length += 1
        if self.length > self.k:
            cur = self.queue.popleft()
            if cur == self.value:
                self.count -= 1
        if num == self.value:
            self.count += 1
        return self.count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)