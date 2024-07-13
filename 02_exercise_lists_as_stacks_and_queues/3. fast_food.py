from collections import deque

qty_of_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders and orders[0] <= qty_of_food:
    qty_of_food -= orders.popleft()

if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")
