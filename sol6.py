data = open("day6", "r")
groups = data.read().split("\n\n")
def inAllSublists(L,x):
    there = True
    for i in L:
        if x not in i:
            there = False
            break
    return there


# Part I
#countTot = 0
#for group in groups:
#    countGroup = 0
#    answers = ""
#    for answer in group:
#        if answer.isalpha() and answer not in answers:
#           answers += answer
#           countGroup += 1
#    countTot += countGroup
#print(countTot)

# Part 2
countTot = 0
countTotAlt = 0
for group in groups[:-1]:
    people = group.split('\n')
    fullYes = people[0]
    yesGroupCount = 0
    for yes in fullYes:
        yesGroupCount += int(inAllSublists(people,yes))
        countTotAlt += int(group.count(yes) == len(people))
    countTot += yesGroupCount
print(countTot)
print(countTotAlt)
lines = groups[-1].split('\n')
dd = lines[0]
tt = 0
for d in dd:
    if d in lines[1]:tt+=1
print(tt)
countTot = 0
for group in groups:
    people = group.split('\n')
    allyes = list(people[0])
    for person in people:
        for yes in allyes:
            if yes not in person:
                allyes.remove(yes)
    countTot += len(allyes)
print(countTot)
