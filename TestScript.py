def getIslands(data):
    numIslands = 0
    visitedValues = [0]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] not in visitedValues:
                numIslands += 1
                visitedValues.append(data[i][j])
            if data[i][j] == 0:
                continue
            if data[i][j] in visitedValues:
                continue
    return numIslands


if __name__ == '__main__':
    matrix = [[1, 1, 1, 0, 3, 0],
              [1, 1, 0, 3, 3, 3],
              [1, 0, 0, 0, 3, 0],
              [4, 4, 4, 0, 0, 0],
              [0, 0, 0, 0, 6, 6],
              [0, 5, 0, 0, 6, 6],
              [5, 5, 5, 0, 0, 6],
              [5, 5, 5, 0, 0, 6]]

    getIslands(matrix)


    print()
