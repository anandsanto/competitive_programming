for t in range(int(input())):
    n = int(input())
    dat = input()
    result = []
    last = None

    for i in range(n-1, -1, -1):
        if last is None:
            last = i
            curlen = 1
            continue
        if dat[i] >= dat[last]:
            result += [str(i) for i in range(1, curlen+1)][::-1]
            curlen = 1
        else:
            curlen += 1
        last = i
    result += [str(i) for i in range(1, curlen+1)][::-1]
    print(f'Case #{t}: {" ".join(result[::-1])}')
