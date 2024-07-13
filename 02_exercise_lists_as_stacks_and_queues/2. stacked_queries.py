n = int(input())
list_stack = []

for i in range(n):
    command = input().split()
    
    if command[0] == '1':
        list_stack.append(int(command[1]))

    elif list_stack:
        if command[0] == '2':
            list_stack.pop()

        elif command[0] == '3':
            print(max(list_stack))

        elif command[0] == '4':
            print(min(list_stack))


print(', '.join([str(x) for x in reversed(list_stack)]))
