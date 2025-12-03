def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def main(start, remainingLst, total):
    for current in remainingLst:
        pos = current[0]
        num = int(current[1:]) % 100
        turns = int(current[1:]) // 100
        total += turns
        turned = False

        if pos == "L":
            leftover = start - num
        
            if leftover < 0:
                if start != 0:
                    total += 1
                start = 100 + leftover
                turned = True
            else:
                start = leftover

        if pos == "R":
            leftover = start + num

            if leftover > 99:
                total += 1
                start = leftover - 100
                turned = True
            else:
                start = leftover
        
        if start == 0 and not turned:
            total += 1
    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(50, lst, 0)
    print(result)
