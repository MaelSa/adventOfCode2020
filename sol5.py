def toBin(p):
    row = ""
    column = ""
    for i in range(7):
        if p[i] == "F":
            row += "0"
        elif p[i] == "B":
            row += "1"
    for i in range(7,10):
        if p[i] == "L":
            column += "0"
        elif p[i] == "R":
            column += "1"
    return int(row,2),int(column,2)
def toBinTot(p):
    tot = ""
    for i in range(10):
        if p[i] in ["F","L"]:
            tot += "0"
        else:
            tot += "1"
    return int(tot,2)

data = open("day5", "r")
passes = data.read().split("\n")[:-1]
listID = []
listtot = []
for p in passes:
    listtot.append(toBinTot(p))
    row, col = toBin(p)
    listID.append(row*8 + col)
for i in range(min(listtot), max(listtot)):
    if i not in listtot:
        print(listID[listtot.index(i-1)])
