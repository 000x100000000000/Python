# This program displays a triangle pattern.
base_size = 8
star_point = base_size

for r in range(base_size):
    for c in range(r):
        print(" ", end="")

    for j in range(star_point):
        print("*", end="")
        
    print()
    star_point -= 1
