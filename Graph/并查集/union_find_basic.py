class UnionFindBasic:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
    
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            return self.find(self.parents[x])
        else:
            return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        
        self.parents[root_x] = root_y 
        return True