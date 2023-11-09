# 1 - 100 doors
# doors = [False] * 101
#
# for i in range(1, 101):
#     for j in range(i, 101, i):
#         doors[j] = not doors[j]
#
# for i in range(1, 101):
#     if doors[i] is True:
#         print(i, end=", ")


# 2 - FizzBuzz
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizz, buzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)