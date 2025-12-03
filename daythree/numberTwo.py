def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main(lst):
    total = 0
    batRange = 12

    for strCode in lst:
        highest = []
        
        startPos = len(highest)

        for pos in range(batRange):
            highest.append('0')
            
            last = batRange - (pos + 1)

            if last == 0:
                rng = strCode[startPos:]
            else:
                rng = strCode[startPos: -last]
            
            
            maxNum = max(rng)
            maxPos = rng.index(maxNum)
            
            if int(maxNum) > int(highest[pos]):
                highest[pos] = maxNum
                startPos += maxPos + 1

        result = ''.join(highest)
        total += int(result)

    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
