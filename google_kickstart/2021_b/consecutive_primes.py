import numpy as np

def prime_array(maxval):
    allnums =  np.array([True] * (maxval+1000))
    allnums[0] = False
    allnums[1] = False
    for i in range(2, len(allnums)):
        if not allnums[i]:
            continue
        if i > maxval:
            updateinds = np.arange(i+1, maxval+1000, 1)
            allnums[updateinds] = False
            break
        else:
            updateinds = np.arange(2*i, maxval+1000, i)
        allnums[updateinds] = False
    return np.argwhere(allnums==True).flatten()


for t in range(int(input())):
    z = int(input())
    maxval = int(z**0.5)

    primelist = prime_array(int(maxval**0.5)+300)

    before = []
    cur = maxval
    while len(before) < 2:
        if 0 not in [cur%i for i in primelist if i != cur]:
           before.append(cur)
        cur -= 1


    after = []
    cur = maxval + 1
    while len(after) < 1:
        if 0 not in [cur%i for i in primelist if i != cur]:
           after.append(cur)
        cur += 1

    out = after + before

    out = out[::-1]

    res = out[-1] * out[-2]
    if res > z:
        res = out[-3] * out[-2]
    print(f"Case #{t+1}: {res}")
