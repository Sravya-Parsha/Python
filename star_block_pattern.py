stars = 5
blocks = 3
lines = 4

for i in range(blocks):
    for j in range(lines - i):
        print("*" * stars)
    print("-" * stars)
