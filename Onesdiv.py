n = int(input())
ones = 1
while ones % n != 0:
    ones = ones * 10 + 1
print(ones)
