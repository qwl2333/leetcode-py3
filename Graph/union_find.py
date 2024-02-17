class UnionFind:
    def __init__(self, N: int):
        self.parents = list(range(N)) # [i for i in range(N)] 也可以

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])
            # path compression
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int):
       self.parents[self.find(x)] = self.find(y)


