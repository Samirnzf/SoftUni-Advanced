numbers = tuple(float(num) for num in input().split())
counter = {}
for number in numbers:
    counter[number] = numbers.count(number)

for key, value in counter.items():
    print(f'{key:.1f} -> {value} times')
