def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line for line in f]

def convertToCols(lst):
    newLst = [[]]
    

    for line in lst:
        value = ""
        colNum = 0

        for char in line.strip():
            if char in ['+', '*']:
                newLst[colNum].append(char)
                colNum += 1
            elif char.isnumeric():
                value += char
            else:
                if value == "":
                    continue

                newLst[colNum].append(int(value))
                colNum += 1
                value = ""

                if colNum >= len(newLst):

                    newLst.append([])
        
        if value != "":
            newLst[colNum].append(int(value))

    return newLst

def main(lst):
    total = 0
    
    lst = convertToCols(lst)

    for row in lst:
        operator = row[-1]
        nums = row[:-1]
        
        sumNum = 0

        if operator == "*":
            sumNum = 1

        for num in nums:
            if operator == "+":
                sumNum += num
            if operator == "*":
                sumNum *= num
        
        total += sumNum
    
    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
