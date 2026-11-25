n =0
for i in range(1,1789):
    if i % 6 == 0 or i % 15 == 0:
        if not(i % 6 == 0 and i % 15 == 0):
            print(i)
            n=n+1
print(n)