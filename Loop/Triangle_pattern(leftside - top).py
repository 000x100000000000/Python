# This program displays a trinagle pattern.
base_size = 8

star_point = 1

for x in range(base_size, 0, -1):
    for y in range(x-1):
        print(" ", end='')

    for z in range(0, star_point):
        print("*", end='')

    print()
    star_point += 1
