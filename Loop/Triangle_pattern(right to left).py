base_size = 8

start = 1

for x in range(base_size, 0, -1):
    for y in range(x-1):
        print(" ", end='')

    for z in range(0, start):
        print("*", end='')

    print()
    start += 1
