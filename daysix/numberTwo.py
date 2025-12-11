def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line for line in f]

def convertToCols(lst):
    lastLine = lst[-1]
    delimiters = []
    
    for en, char in enumerate(lastLine):
        if en == 0:
            delimiters.append(0)
        elif char in ['+', '*']:
            delimiters.append(en)
    
    newLst = [[] for _ in range(len(delimiters))]
    
    for col, row in enumerate(lst):
        first = 0
        last = delimiters[-1]

        for en, delimiter in enumerate(delimiters):
            x = 0
            if delimiter == first:
                x = row[0:delimiters[1] - 1]
            elif delimiter == last:
                x = row[last:].replace('\n', '')
            else:
                x = row[delimiter:delimiters[en + 1] -1]
            
            newLst[col].append(x)
    
    convertedLst = [[] for _ in range(len(newLst[0]))]
    for row in newLst:
        for en, chars in enumerate(row):
            convertedLst[en].append(chars)
    
    newLst = [[] for _ in range(len(delimiters))]
    
    operators = [char for char in lastLine if char not in [' ', '\n']]
    
    for en, col in enumerate(convertedLst):
        for colLen in list(reversed(range(len(col[0])))):
            newNum = ''
            for char in col:
                if char[colLen] not in [' ', '+', '*']:
                    newNum += char[colLen]

            newLst[en].append(int(newNum))
    
    
    for en, row in enumerate(newLst):
        row.append(operators[en])

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
