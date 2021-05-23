t = int(input())

for case in range(1, t+1):
    n, k = [int(i) for i in input().strip().split()]
    inpstr = input()
    revinpstr = inpstr[::-1]
    tot = 0
    for ind in range(1, (n//2) + 1):
        tot += int(inpstr[ind-1] != revinpstr[ind-1])
    print(f"Case #{case}: {abs(k - tot)}")
