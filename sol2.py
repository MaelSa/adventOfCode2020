data = open("day2","r")
L = sorted([i for i in data.read().split('\n')[:-1]])
correctPass = 0
for line in L:
    line = line.split()
    ranges = line[0].split('-')
    low, top = int(ranges[0]), int(ranges[1])
    char = line[1][0]
    if int(line[-1][low-1]==char) + int(line[-1][top-1]==char) == 1:
        correctPass += 1
print(correctPass)
