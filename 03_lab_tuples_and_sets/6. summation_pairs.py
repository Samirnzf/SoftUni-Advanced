numbers = list(map(int, input().split()))
target_number = int(input())

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_number:
            print(f"{numbers[i]} + {numbers[j]} = {target_number}")
            numbers.remove(numbers[i])
            numbers.remove(numbers[j])