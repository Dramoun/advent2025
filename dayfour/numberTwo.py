def readFile(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main(lst):
    total = 0
    roomMap = []
    rollRemoved = True
    lastTotal = 0

    for en, space in enumerate(lst):
        roomMap.append([])
        for item in space:
            roomMap[en].append(item)
            
    while rollRemoved:
        for row, rowData in enumerate(roomMap):
            for col in range(len(rowData)):
                friends = returnFriends(row, col, roomMap)
            
                if friends < 4 and roomMap[row][col] == '@':
                    total += 1
                    roomMap[row][col] = '.'
        
        if total == lastTotal:
            rollRemoved = False

        lastTotal = total
        
    return total

def returnFriends(row, col, roomMap):
    total = 0 

    friendOffset = [[-1,-1],[-1,0],[-1,1],
                    [0, -1], [0,1],
                    [1, -1], [1, 0], [1,1]]

    friendPos = []

    for offset in friendOffset:
        rowF = offset[0]
        colF = offset[1]
        friendPos.append([row + rowF, col + colF])

    validPos = []

    for pos in friendPos:
        if not pos[0] < 0 and not pos[1] < 0 and not pos[0] > len(roomMap) - 1 and not pos[1] > len(roomMap) - 1 :
            validPos.append(pos)
    
    for pos in validPos:
        rowF = pos[0]
        colF = pos[1]
        friend = roomMap[rowF][colF]
        if friend == '@':
            total += 1
    
    return total

if __name__ == "__main__":
    lst = readFile("./file.txt")
    result = main(lst)
    print(result)
