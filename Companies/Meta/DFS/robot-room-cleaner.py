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
        """
        :type robot: Robot
        :rtype: None
        """
        # Directions: [up, left, down, right]
        dirs = [(-1, 0), (0, -1), (1, 0),(0, 1)]


        cleaned = set()
        '''
        为什么要记录cur_dir
        其实一般的dfs是不在意上次的方向的
        所以每次都是
        for dx, dy in dirs:
        每个循环都是从up, left, down, right
        但是机器人不行, 很难每到一个新的地方你都要调整方向回到up,
        所以最好是记录上次的方向一条道走到黑, 再换一个方向
        dfs_helper可以理解为
        机器人先进入(i,j)这个点
        然后开始clean
        clean完成再从四个方向clean,初始方向和上次的方向一致
        完成之后回到(i,j)的那个店,并且保持将要进入(i,j)的那个方向
        '''
        def dfs_helper(i, j, cur_dir):
            robot.clean()
            cleaned.add((i, j))

            for n_direction in range(cur_dir, cur_dir + 4):
                nx = dirs[n_direction % 4][0] + i
                ny = dirs[n_direction % 4][1] + j
                if (nx, ny) not in cleaned and robot.move():
                    dfs_helper(nx, ny, n_direction % 4)
                # Change orientation
                robot.turnLeft()
            
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        
        dfs_helper(0, 0, 0)

        # [1,1,1,1,1,0,1,1],
        # [1,1,1,1,1,0,1,1],
        # [1,0,1,1,1,1,1,1],
        # [0,0,0,1,0,0,0,0],
        # [1,1,1,1,1,1,1,1]