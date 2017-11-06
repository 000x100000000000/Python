# This program uses nested loops to draw a pattern.
base_size = 6

star_point = 0

for c in range(base_size):
    print("*", end="")
    
    for x in range(c):
        print(" ", end="")
        
    print("*")
