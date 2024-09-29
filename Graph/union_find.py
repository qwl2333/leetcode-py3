class UnionFind:
    def __init__(self, N: int):
        self.parents = list(range(N)) # [i for i in range(N)] 也可以
        self.ranks = [1 for _ in range(N)]
    # recursion
    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        else:
            # return self.find(self.parents[x])

            # path compression
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # iterative
    '''
    The time complexity of the Find operation, when using path compression, 
    is nearly constant and is bounded by O(α(n)), 
    where α(n) is the inverse Ackermann function. For all practical purposes, 
    this grows extremely slowly, and even for very large inputs, it can be considered as close to constant time.
    '''
    def find2(self, x: int) -> int:
        root = x
        # find the root node of x
        while root != self.parents[root]:
            root = self.parents[root]
        
        # path compression: make all ancestors point directly to root
        while x != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        
        return root
    
    '''
    The time complexity of the Union operation, when using union by rank or size, is also O(α(n)) because the depth of any tree is limited by the inverse Ackermann function.
    '''
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: # 不能merge 两个集合，因为有环
           return False
        else:
            if self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
            elif self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
            else:
                self.parents[root_x] = root_y
                self.ranks[root_y] += 1
            return True