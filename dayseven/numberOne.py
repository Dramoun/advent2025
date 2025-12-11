def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line for line in f]


def main(lst):
    total = 0
    
    startCol = lst[0].index('S')
    beamList = set()

    beamList.add(startCol)
    
    for row in lst[1:]:
        beamList, added = updateBeamList(beamList, row)
        
        for en, char in enumerate(row):
            if en in  beamList:
                row = row[:en] + '|' + row[en + 1:]

        print(row)
        print(added)
        total += added

    return total

def updateBeamList(beamList, row):
    newBeamList = set()
    added = 0

    for beam in beamList:
        if row[beam] != '^':
            newBeamList.add(beam)
        else:
            if beam - 1 >= 0 and beam - 1 not in newBeamList and beam - 1 not in beamList:
                #print('adding ', beam - 1, 'to', newBeamList)
                newBeamList.add(beam - 1)
            if beam + 1 <= len(row) - 1 and beam + 1 not in newBeamList and beam + 1 not in beamList:
                #print('adding ', beam + 1, 'to', newBeamList)
                newBeamList.add(beam + 1)
            added += 1 
    
    return newBeamList, added

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
