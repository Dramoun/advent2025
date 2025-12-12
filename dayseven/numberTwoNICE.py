def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line for line in f]


def main(lst):
    total = 0
    
    startCol = lst[0].index('S')
    x = travelUniverse([startCol], lst[1:])
    
    for universe in x:
        print('=============================================')
        for row, col in enumerate(universe):
            row = lst[row]
            row = row[:col] + '|' + row[col + 1:]
            print(row)
    return len(x)

def travelUniverse(pastSteps, futurePaths):
    if not futurePaths:
        return [pastSteps]

    allPaths = []

    lastPos = pastSteps[-1]
    nextRow = futurePaths[0]
    nextStep = nextRow[lastPos]
    followingPaths = futurePaths[1:]

    left = lastPos - 1
    right = lastPos + 1

    if nextStep == "^":
        
        if left >= 0:
            anotherStep = pastSteps + [left]
            allPaths += travelUniverse(anotherStep, followingPaths)
        
        if right < len(nextRow):
            anotherStep = pastSteps + [right]
            allPaths += travelUniverse(anotherStep, followingPaths)

    else:
        anotherStep = pastSteps + [lastPos]
        allPaths += travelUniverse(anotherStep, followingPaths)

    return allPaths
if __name__ == "__main__":
    lst = readFile("./test.txt")
    result = main(lst)
    print(result)
