from collections import deque


queue = deque(input().split())
n = int(input())

while len(queue) > 1:
    queue.rotate(1-n)
    print(f"Removed {queue.popleft()}")
else:
    print(f"Last is {queue.pop()}")
