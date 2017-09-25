import random

n = random.randint(2,100)
print(n)
with open('2261-4.input', 'w') as f:
    f.write(str(n) + "\n")
    for _ in range(n):
        f.write(str(random.randint(-1000,1000)) + " " + str(random.randint(-1000,1000)) + "\n")