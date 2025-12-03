def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def filterToList(lst):
    return lst[0].split(',')


def divisors(n: int) -> list[int]:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)

def main(lst):
    total = 0

    for duo in lst:
        minum, maxnum = duo.split('-')
        
        for num in range(int(minum), int(maxnum)+1):
            strNum = str(num)
            numLen = len(strNum)
            included = set()
            
            divs = divisors(numLen)[:-1]

            for base in divs:
                combo = str(strNum[:base]) * int(numLen / base)
                
                if combo == str(num) and num not in included:
                    total += num
                    included.add(num)
                    
            
    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(filterToList(lst))
    print(result)
