numbers = (
    1, 4, 5, 3, 3, 7, 2, 10
)

print(
    len(numbers)
)

print(
    # genera una nueva lista
    sorted(numbers) # list (default=asc)
)

print(
    sorted(numbers, reverse=True)
)

print(
    # numbers.count(1000) --> devuelve 0
    numbers.count(3)
)

# True --> 1
print(
    # 3 in numbers # True / False
    # True in numbers
    100 in numbers
)

print(
    numbers.index(4)
)