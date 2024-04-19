# lc 1166

class FileSystem:

    def __init__(self):
        self.map = {} # path: value

    # Time O(n) n is length the path, space O(n^2) n is length of the path because
    # we create extra str each level 1, 2, 3 ... n
    def createPath(self, path: str, value: int) -> bool:
        if path in self.map:
            return False

        nodes = path.split('/')[1:]
        def dfs(idx: int, prev_path: str) -> bool:
            cur_path = prev_path + '/' + nodes[idx]
            if cur_path == path:
                self.map[path] = value
                return True

            if cur_path not in self.map:
                return False

            return dfs(idx + 1, cur_path)
        
        return dfs(0, '')
            

    def get(self, path: str) -> int:
        if path in self.map:
            return self.map[path]
        else:
            return -1
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)