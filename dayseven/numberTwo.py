def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line for line in f]


def main(lst):
    total = 0
    
    startCol = lst[0].index('S')
    beamList = set()

    beamList.add(startCol)
    
    updatedBeamList = []

    for row in lst[1:]:
        beamList, split = updateBeamList(beamList, row)
        
        if split > 0:
            for en, char in enumerate(row):
                if en in  beamList:
                    row = row[:en] + '|' + row[en + 1:]
            
            rowDiffTotal = 0

            print(row.strip())
            print(split, beamList)
        
            total += split

    return total

def updateBeamList(beamList, row):
    newBeamList = set()
    split = 0

    for beam in beamList:
        if row[beam] != '^':
            newBeamList.add(beam)
        else:
            left = beam - 1
            right = beam + 1

            if left not in beamList:
                #print('adding ', beam - 1, 'to', newBeamList)
                newBeamList.add(beam - 1)
                split += 1 
            
            if right not in beamList:
                #print('adding ', beam + 1, 'to', newBeamList)
                newBeamList.add(beam + 1)
                split += 1 
                
    return newBeamList, split

if __name__ == "__main__":
    lst = readFile("./test.txt")
    result = main(lst)
    print(result)
