'''As string'''

string_input = input()
reversed_string = string_input[::-1]
print(reversed_string)

''' As stack '''

text = list(input())
while text:
    print(text.pop(), end='')
