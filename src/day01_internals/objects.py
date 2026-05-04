x = 10
y = x

print("x:", x, "id:", id(x))
print("y:", y, "id:", id(y))

y = y + 1

print("\nAfter modifying y:")
print("x:", x, "id:", id(x))
print("y:", y, "id:", id(y))