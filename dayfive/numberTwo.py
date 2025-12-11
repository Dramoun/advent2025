def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line for line in f]

def splitList(lst: list):
    one = []
    two = []

    split = False

    for line in lst:
        if line == "\n":
            split = True
            continue
        if split:
            two.append(line.strip())
        else:
            one.append(line.strip())

    return [one, two]

def main(lst):
    total = 0
    ranges, ids = splitList(lst)
    newRange = []
    
    ranges.sort(key=sortRanges)

    for duo in ranges:
        low, high = duo.split('-')
        newRange = into(low, high, newRange)        

    for ran in newRange:
        rn = len(range(ran[0], ran[1] + 1))
        total += rn

    return total
def sortRanges(e):
    return int(e.split('-')[0])

def into(low, high, newRange):
    low = int(low)
    high = int(high)
    added = False

    for item in newRange:
        minimum = item[0]
        maximum = item[1]
        
        if high < minimum or low > maximum:
           continue 
        
        if low <= minimum:
            if high >= minimum:
                if high <= maximum:
                    item[0] = low
                    added = True
                    break

        if low >= minimum and low <= maximum:
            if high >= minimum and high <= maximum:
                added = True
                break

        if high >= maximum:
            if low >= minimum:
                if low <= maximum:
                    item[1] = high
                    added = True
                    break

        if low <= minimum and high >= maximum:
            item[0] = low
            item[1] = high
            added = True
            break

    if not added:
        newRange.append([low, high])
    
    return newRange

if  __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
