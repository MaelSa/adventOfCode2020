data = open("day3", "r")
data = data.read().split("\n")
encounteredTrees = [ 0 for i in range(5)]
pos = [0 for i in range(5)]
even = True
for line in data[:-1]:
    for i in range(4):
        if line[pos[i]%len(line)] == "#":encounteredTrees[i]+=1
    pos[0]+= 1
    pos[1] += 3
    pos[2] += 5
    pos[3] += 7
    if even:
        if line[pos[4]%len(line)] == '#':encounteredTrees[4]+=1
        pos[4]+=1
    even = not even
r = 1
for i in encounteredTrees:r*=i
print(r)
#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2
