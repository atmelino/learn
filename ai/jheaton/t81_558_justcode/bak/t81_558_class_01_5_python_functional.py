def process_string(str):
    t = str.strip()
    return t[0].upper()+t[1:]

str = process_string("  hello  ")
print(f'"{str}"')

l = ['   apple  ', 'pear ', 'orange', 'pine apple  ']
mylist=list(map(process_string, l))
print("print(mylist)",mylist)
print("print(*mylist)",*mylist)
print("print(mylist[:])",mylist[:])
print("print(mylist[1:-1])",mylist[1:-1])

l = ['   apple  ', 'pear ', 'orange', 'pine apple  ']
l2 = [process_string(x) for x in l]
print(l2)


def greater_than_five(x):
    return x>5

l = [ 1, 10, 20, 3, -2, 0]
l2 = list(filter(greater_than_five, l))
print(l2)

l = [ 1, 10, 20, 3, -2, 0]
l2 = list(filter(lambda x: x>5, l))
print(l2)


from functools import reduce

l = [ 1, 10, 20, 3, -2, 0]
result = reduce(lambda x,y: x+y,l)
print(result)







