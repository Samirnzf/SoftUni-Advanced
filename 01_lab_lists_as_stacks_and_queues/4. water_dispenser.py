from collections import deque

liters_of_water = int(input())
queue = deque([])

while True:
    name = input()
    queue.append(name)

    if name == 'Start':
        break

while True:
    command = input()

    if command == 'End':
        break

    if command.isdigit():
        liters_wanted = int(command)
        person = queue.popleft()

        if liters_of_water >= liters_wanted:
            liters_of_water -= liters_wanted
            print(f"{person} got water")
        else:
            print(f'{person} must wait')

    else:
        _, liters_to_refill = command.split()
        liters_to_refill = int(liters_to_refill)
        liters_of_water += liters_to_refill

print(f'{liters_of_water} liters left')
