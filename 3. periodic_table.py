# number_of_elements = int(input())
#
# unique_elements = set()
#
# for _ in range(number_of_elements):
#     for element in input().split():
#         unique_elements.add(element)
#
# print(*unique_elements, sep='\n')

print(*{el for _ in range(int(input())) for el in input().split()}, sep='\n')
