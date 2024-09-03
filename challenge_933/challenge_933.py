from collections import deque


class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        return self.requests_in_past_3000()
    
    def requests_in_past_3000(self) -> int:
        while self.requests and self.requests[0] < self.requests[-1] - 3000:
            self.requests.popleft()
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)