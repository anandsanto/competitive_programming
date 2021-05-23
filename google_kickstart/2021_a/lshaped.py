import numpy as np

class Node:
    def __init__(self):
        self.top = None
        self.left = None
        self.right = None
        self.bottom = None

    def __repr__(self):
        return f"T: {self.top} B: {self.bottom} R: {self.right} L: {self.left}"


def get_num_ls(pair):
    a = pair[0]
    b = pair[1]
    num = 0
    if min(a//2, b) >= 2:
        num = min(a//2, b) - 1

    if min(b//2, a) >= 2:
        num += min(b//2, a) - 1

    return num

nodegrid = []
for i in range(1000):
    nodegrid.append([])
    for j in range(1000):
        nodegrid[-1].append(Node())


for t in range(1, int(input())+1):
    r, c = [int(i) for i in input().split()]
    grid = [[int(i) for i in input().split()] for j in range(r)]

    for i in range(r):
        left_num = 1
        for j in range(c):
            if grid[i][j] == 1:
                nodegrid[i][j].left = left_num
                left_num += 1
            else:
                left_num = 1

    for i in range(r):
        right_num = 1
        for j in range(c-1, -1, -1):
            if grid[i][j] == 1:
                nodegrid[i][j].right = right_num
                right_num += 1
            else:
                right_num = 1

    for j in range(c):
        top_num = 1
        for i in range(r):
            if grid[i][j] == 1:
                nodegrid[i][j].top = top_num
                top_num += 1
            else:
                top_num = 1

    for j in range(c):
        bot_num = 1
        for i in range(r-1, -1, -1):
            if grid[i][j] == 1:
                nodegrid[i][j].bottom = bot_num
                bot_num += 1
            else:
                bot_num = 1


    tot = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                continue
            node = nodegrid[i][j]
            tot += get_num_ls((node.left, node.top))
            tot += get_num_ls((node.left, node.bottom))
            tot += get_num_ls((node.right, node.bottom))
            tot += get_num_ls((node.right, node.top))

    print(f"Case #{t}: {tot}")
