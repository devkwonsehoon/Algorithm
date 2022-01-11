color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

first = color.index(input())
second = color.index(input())
multiple = color.index(input())

result = int(str(first) + str(second)) * (10 ** multiple)
print(result)