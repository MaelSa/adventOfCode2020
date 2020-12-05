def isHexa(h):
    chars = '0123456789abcdef'
    hexa = True
    for c in h:
        if c not in chars:
            hexa = False
            break
    if len(h) != 6:
        hexa = False
    return hexa


data = open("day4", "r")
possibleAttributes = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
attributeConditions = {
    'byr': [str(i) for i in range(1920,2003)],
    'iyr': [str(i) for i in range(2010,2021)],
    'eyr': [str(i) for i in range(2020,2031)],
    'hgtcm': [str(i) for i in range(150,194)],
    'hgtin': [str(i) for i in range(59,77)],
    'ecl' : ['amb','blu','brn','gry','grn','hzl','oth']
}
passports = data.read().split("\n\n")
validPassports = 0
for passport in passports:
    containedAttr = []
    passAttr = passport.split()
    for attr in passAttr:
        attrName = attr.split(':')[0]
        attrValue = attr.split(':')[1]
        if (attrName in possibleAttributes) and (attrName not in containedAttr):
            if attrName == 'hgt':
                if attrValue[-2:] == 'cm':
                    if attrValue[:-2] in attributeConditions['hgtcm']:
                        containedAttr.append(attrName)
                    else:
                        break
                elif attrValue[-2:] == 'in':
                    if attrValue[:-2] in attributeConditions['hgtin']:
                        containedAttr.append(attrName)
                    else:
                        break
                else:
                    break
            elif  attrName == 'hcl':
                if attrValue[0]=='#' and isHexa(attrValue[1:]):
                    containedAttr.append(attrName)
                else:
                    break
            elif attrName == 'pid':
                if len(attrValue) == 9 and attrValue.isnumeric():
                    containedAttr.append(attrName)
                else:
                    break
            elif attrName == 'cid':
                containedAttr.append(attrName)
            elif attrValue in attributeConditions[attrName]:
                containedAttr.append(attrName)
            else:
                break
    if len(containedAttr)==8 or (len(containedAttr)==7 and 'cid' not in containedAttr):
        validPassports += 1
print(validPassports)

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)
