from itertools import product
import heapq

for t in range(1, int(input())+1):
    r, c = [int(i) for i in input().split()]
    grid = [[int(i) for i in input().split()] for j in range(r)]
    weights = [(-1*grid[i][j], (i,j)) for i in range(r) for j in range(c)]
    heapq.heapify(weights)

    visited = set()

    blocks_added = 0

    while len(weights) > 0:

        height, (x, y) = heapq.heappop(weights)

        height *= -1

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x > 0:
            if grid[x-1][y] < height:
                blocks_added += (height - grid[x-1][y] - 1)
                if blocks_added > 0:
                    grid[x-1][y] = height - 1
                    heapq.heappush(weights, (1-height, (x-1, y)))
        if x < r-1:
            if grid[x+1][y] < height:
                blocks_added += (height - grid[x+1][y] - 1)
                if blocks_added > 0:
                    grid[x+1][y] = height - 1
                    heapq.heappush(weights, (1-height, (x+1, y)))
        if y > 0:
            if grid[x][y-1] < height:
                blocks_added += (height - grid[x][y-1] - 1)
                if blocks_added > 0:
                    grid[x][y-1] = height - 1
                    heapq.heappush(weights, (1-height, (x, y-1)))
        if y < c-1:
            if grid[x][y+1] < height:
                blocks_added += (height - grid[x][y+1] - 1)
                if blocks_added > 0:
                    grid[x][y+1] = height - 1
                    heapq.heappush(weights, (1-height, (x, y+1)))


    print(f"Case #{t}: {blocks_added}")
