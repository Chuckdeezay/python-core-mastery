# Immutable example
a = 100
b = a

b += 50

print("a:", a)
print("b:", b)

# Mutable example
list1 = [1, 2, 3]
list2 = list1

list2.append(4)

print("\nlist1:", list1)
print("list2:", list2)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # ?
print(a is c)  # ?
print(a is b)  # ?