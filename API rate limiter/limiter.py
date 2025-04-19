#Design a system that limits the number of requests a user can make within a time window
#We want to allow N requests per T seconds cper user
#for each user we want to track the timestamps of their recent requests
#we would use a sliding window
#we will remove any timestamps older than T seconds
#we would only allow a request id=f the total number of requests in under N

#In a rate limiter we would create a limiter call then a function that can used to check if a user can make a request
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        #users are the keys and value are the time stamp of their use requests storeed in a deque
        self.user_requests = defaultdict(deque)

    def is_request_allowed(self, user_id: str, timestamp: int) -> bool:
        usages = self.user_requests[user_id]

        while usages and timestamp - usages[0] >= self.time_window:
            usages.popleft()

        if len(usages) < self.max_requests:
            usages.append(timestamp)
            return True
        return False
    

limiter = RateLimiter(max_requests=3, time_window=10)

print(limiter.is_request_allowed("alice", 1))   # True
print(limiter.is_request_allowed("alice", 2))   # True
print(limiter.is_request_allowed("alice", 3))   # True
print(limiter.is_request_allowed("alice", 4))   # False (limit reached)
print(limiter.is_request_allowed("alice", 12))  # True (old ones expired)
