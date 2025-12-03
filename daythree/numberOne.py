def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main(lst):
    total = 0
    

    for strLine in lst:
        first = '0'
        firstEn = 0
        second = '0'
        
        for order in range(2):
            
            for en, strNum in enumerate(strLine):
                num = int(strNum)
                
                if order == 0 and en != (len(strLine) - 1):
                    if num > int(first):
                        first = strNum
                        firstEn = en + 1
                
                if order == 1:
                    if num > int(second):
                        second = strNum
            
            strLine = strLine[firstEn:]
        
        result = int(first + second)
        total += result

    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
