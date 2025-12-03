def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def filterToList(lst):
    return lst[0].split(',')

def main(lst):
    total = 0

    for duo in lst:
        minum, maxnum = duo.split('-')

        for num in range(int(minum), int(maxnum)+1):
            strNum = str(num)
            numLen = len(strNum)
            rest = int(numLen % 2)
            
            if rest == 1:
                continue
            
            half = int(numLen / 2)
            first = strNum[:half]
            second = strNum[half:]

            if first == second:
                total += int(strNum)
            
    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(filterToList(lst))
    print(result)
