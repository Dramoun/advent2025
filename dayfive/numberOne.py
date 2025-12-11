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
    
    for _id in ids:
        for duo in ranges:
            lessThen, moreThen = duo.split('-')
            
            if int(lessThen) <= int(_id) <= int(moreThen):
                total += 1
                break

    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
