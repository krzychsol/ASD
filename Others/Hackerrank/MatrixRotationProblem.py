def matrixRotation(matrix, r):
    rows = len(matrix)
    cols = len(matrix[0])
    layers = min(rows,cols)//2

    for _ in range(r):
        for i in range(layers):
            circle = []
            first = matrix[i][i]

            for k in range(i,cols-1-i):
                #circle.append(matrix[i][k])
                matrix[i][(k+1)%cols] = matrix

            for k in range(i,rows-1-i):
                pass
                # circle.append(matrix[k][cols-1-i])

            for k in range(cols-1-i,i,-1):
                pass
                # circle.append(matrix[rows-1-i][k])

            for k in range(rows-1-i,i,-1):
                pass
                # circle.append(matrix[k][i])

            n = len(circle)
            first = circle[0]
            for i in range(n-1,0,-1):
                circle[(i+1)%n] = circle[i]
            circle[1] = first

            cnt = 0
            for k in range(i, rows - i - 1):
                matrix[k][i] = circle[cnt]
                cnt += 1

            for k in range(i, cols - i - 1):
                matrix[rows - 1 - i][k] = circle[cnt]
                cnt += 1

            for k in range(rows - i - 1, i, -1):
                matrix[k][cols - 1 - i] = circle[cnt]
                cnt += 1

            for k in range(cols - 1 - i, i, -1):
                matrix[i][k] = circle[cnt]
                cnt += 1

    return matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotated = matrixRotation(matrix,2)
for el in rotated:
    print(el)

    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 16



