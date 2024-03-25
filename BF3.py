import random 
random.seed(320)

n = 100
a = [1, 2, 3, 4, 5, 6, 7, 8] 
b = [8, 7, 6, 5, 4, 3, 2, 1]

blooms = {2:[0] * (8 * n), 
          4:[0] * (8 * n),
          6:[0] * (8 * n),
          8:[0] * (8 * n)}

for i in range(n):
    x = random.randint(0, 2**31)
    for j in range(8):
        v = (a[j] + b[j] * x) % (8 * n)
        if j < 2:
            blooms[2][v] = 1
        if j < 4:
            blooms[4][v] = 1
        if j < 6:
            blooms[6][v] = 1
        if j < 8:
            blooms[8][v] = 1

counts = {2:0, 4:0, 6:0, 8:0}

while True:
    try:
        new = int(input())
    except:
        break
    else:
        for k in (2, 4, 6, 8):
            for j in range(k):
                v = (a[j] + b[j] * new) % (8 * n)
                if blooms[k][v] == 0:
                    counts[k] += 1
                    break

print(counts[2])
print(counts[4])
print(counts[6])
print(counts[8])