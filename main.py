from calculator import sum

# print(sum(10, 20))
# print(sum('s', 20))

try:
    print(sum('s', 10), 20)
except AssertionError as e:
    print(f'Error: {e}')
