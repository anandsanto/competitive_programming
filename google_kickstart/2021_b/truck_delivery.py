import sys
sys. setrecursionlimit(100001)

class SegNode:
    def __init__(self, start_range: int, end_range: int, value):
        self.start_range = start_range
        self.end_range = end_range
        self.value = value
        self.size = end_range - start_range + 1

    def __repr__(self):
        return f'{self.start_range} -- {self.end_range}: {self.value}'


class SegTree:

    def __init__(self, N: int, mergefun: callable):
        self.N = N
        exp = 0
        while N:
            N = N>>1
            exp += 1
        self.array = [None] * 2**(exp+1)
        self.mergefun = mergefun
        self.populate(0, self.N, 0)

    def populate(self, start, end, ind):
        self.array[ind] = SegNode(start, end, 0)
        if start == end:
            return
        self.populate(start, start + (end-start)//2, 2*ind + 1)
        self.populate(start + (end-start)//2 + 1, end, 2*ind + 2)

    def insert(self, index, value, at=0):
        if self.array[at].size == 1:
            self.array[at].value = value
            return
        node = self.array[at]
        start = node.start_range
        end = node.end_range
        mid = start + (end-start)//2
        if index <= mid:
            self.insert(index, value, 2*at+1)
        else:
            self.insert(index, value, 2*at+2)

        merged = self.mergefun(self.array[2*at+1].value, self.array[2*at+2].value)
        node.value = merged


    def query(self, start, end, at=0):

        node = self.array[at]
        nodestart = node.start_range
        nodeend = node.end_range
        mid = nodestart + (nodeend-nodestart)//2

        if start <= nodestart and end >= nodeend:
            return node.value

        if start >= nodestart and end <= mid:
            return self.query(start, end, 2*at+1)

        if start >= (mid + 1) and end <= end:
            return self.query(start, end, 2*at+2)

        left = self.query(start, mid, 2*at+1)
        right = self.query(mid+1, end, 2*at+2)

        return self.mergefun(left, right)

def dfs(node, parent=None):

    children = [i for i in adj[node].keys() if i != parent]

    if len(children) == 0:
        return

    for i in children:
        tree.insert(adj[node][i][0], adj[node][i][1])
        if i in queries:
            for wt in queries[i]:
                queries[i][wt] = tree.query(0, wt)
        dfs(i, parent=node)
        tree.insert(adj[node][i][0], 0)


def gcd(x, y):
    return y if x== 0 else gcd(y % x, x)


tree = SegTree(int(2*1e5)+1, gcd)


for t in range(int(input())):
    adj = {}
    N, Q = [int(i) for i in input().split()]

    for i in range(N-1):
        x, y, l, a = [int(i) for i in input().split()]
        if x not in adj:
            adj[x] = {}
        adj[x][y] = (l, a)
        if y not in adj:
            adj[y] = {}
        adj[y][x] = (l, a)

    queries = {}
    direct = []

    for i in range(Q):
        c, w = [int(i) for i in input().split()]
        if c not in queries:
            queries[c] = {}
        direct.append((c, w))
        queries[c][w] = None


    dfs(1)

    res = " ".join([str(queries[i[0]][i[1]]) for i in direct])
    print(f"Case #{t+1}: {res}")
