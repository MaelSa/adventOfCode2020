data = open("day1","r")
L = sorted([int(i) for i in data.read().split('\n')[:-1]])
for i in L:
    for j in L:
        for k in L:
            if j+i+k == 2020:
                print(i*j*k)
                break
