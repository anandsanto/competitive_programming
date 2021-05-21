import numpy as np

for t in range(int(input())):
    n = int(input())
    nums = np.array([int(i) for i in input().strip().split()])
    diffnums = np.diff(nums)

    chunks = []
    previ = None
    for i in diffnums:
        if previ is None:
            chunksize = 1
            chunknum = i
            previ = i
            continue
        if previ != i:
            chunks.append((chunknum, chunksize))
            chunknum = i
            chunksize = 1
        else:
            chunksize += 1
        previ = i

    chunks.append((chunknum, chunksize))
    maxlen = 0

    for i in range(len(chunks)):
        for factor in [1, -1]:
            curlen = chunks[i][1] + 1
            if i+1*factor >= 0 and i+1*factor < len(chunks):
                curlen += 1
                if (i+2*factor >= 0 and i+2*factor < len(chunks)) and chunks[i+1*factor][1] == 1:
                    if chunks[i+1*factor][0] + chunks[i+2*factor][0] == 2*chunks[i][0]:
                        curlen += 1
                        if i+3*factor >= 0 and i+3*factor < len(chunks):
                            if chunks[i+3*factor][0] == chunks[i][0]:
                                curlen += chunks[i+3*factor][1]

            maxlen = max(curlen, maxlen)


    print(f'Case #{t+1}: {maxlen}')
