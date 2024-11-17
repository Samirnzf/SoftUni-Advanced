odd_numbers = set()
even_numbers = set()

for i in range(1, int(input()) + 1):
    current_score = sum(ord(letter) for letter in input()) // i

    if current_score % 2 == 0:
        even_numbers.add(current_score)
    else:
        odd_numbers.add(current_score)

if sum(odd_numbers) == sum(even_numbers):
    print(*odd_numbers.union(even_numbers), sep=", ")

elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=', ')

else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=', ')
