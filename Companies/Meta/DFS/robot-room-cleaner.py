# lc 489 类似 lc 1778 但是1778 dfs 建造图的时候不在乎方向

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        
        # 定义逻辑方向: 0:上, 1:右, 2:下, 3:左 (注意: 这里的顺序是顺时针，方便理解)
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # 记忆：存储已清洁的逻辑坐标
        cleaned = set()
       
        # ----------------------------------------------------
        # 核心回溯函数：转身 180度 -> 前进 -> 转身 180度 (恢复位置和朝向)
        def go_back(robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        # ----------------------------------------------------

        # dfs_helper(i, j, cur_dir)：机器人位于逻辑 (i, j)，面向 cur_dir 索引
        def dfs_helper(i, j, cur_dir):
            robot.clean()
            cleaned.add((i, j))

            # 探索四个方向 (从当前朝向开始顺时针旋转)
            for k in range(4):
                
                # 计算当前物理朝向所对应的逻辑方向索引
                new_dir_idx = (cur_dir + k) % 4
                
                # 计算如果移动成功，应该到达的逻辑坐标
                dx, dy = dirs[new_dir_idx]
                nx, ny = i + dx, j + dy

                # 检查：1. 逻辑上未访问过 2. 物理上可以移动
                if (nx, ny) not in cleaned and robot.move():
                    
                    # 递归深入：将新的坐标和新的方向索引传入
                    dfs_helper(nx, ny, new_dir_idx)
                    
                    # ⚠️ 物理回溯：当子递归返回时，机器人必须回到 (i, j)
                    go_back(robot)
                
                # 每次循环后，物理转向 90度，为下一次循环探索下一个方向做准备
                robot.turnRight()
            
            # 当 for 循环结束，(i, j) 的所有分支都探索完毕，函数返回
            # go_back() 序列的最后一步会确保 robot 在返回给调用者时，朝向是正确的。

        
        # 从 (0, 0) 开始，默认朝向 0 (上)
        dfs_helper(0, 0, 0)

        # [1,1,1,1,1,0,1,1],
        # [1,1,1,1,1,0,1,1],
        # [1,0,1,1,1,1,1,1],
        # [0,0,0,1,0,0,0,0],
        # [1,1,1,1,1,1,1,1]

# 一个node 遍历所有graph里面的节点 打印出来就可以
class Solution2:
    def simple_dfs_traverse(self, start_x, start_y, is_valid_cell):
        # 记忆地图 (存储已访问的 (x, y) 坐标)
        visited = set()
        # 四个探索方向
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

        def dfs(x, y):
            # 1. 标记当前点
            visited.add((x, y))
            print(f"Cleaning: ({x}, {y})") # 执行操作
            
            # 2. 探索周围的四个邻居
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 检查条件 (核心逻辑)
                if (nx, ny) not in visited and is_valid_cell(nx, ny):
                    # 3. 递归深入 (DFS)
                    dfs(nx, ny) 
                    
                    # 4. 算法回溯点：
                    # 当上面的 dfs(nx, ny) 返回时，程序回到这里，
                    # 自动开始检查下一个方向。
                    # 但是物理世界的机器人不像这个graph的遍历仅仅依赖stack的x,y坐标，机器人除了坐标,自己还需要调整位置
                    # 所以才会有go_back(robot) 和 robot.turnRight()
        
        # 从起点开始探索
        dfs(start_x, start_y)
        return visited