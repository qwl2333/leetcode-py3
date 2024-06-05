'''
In Roblox, there is a category of game called "Obby", or Obstacle Courses. Users need to walk and jump around a series of platforms to reach the goal.

In this question, we would like to know if there is a possible route through an obstacle course.

The course is represented by an N x M grid of integers:
- 1 represents a platform and
- 0 represents a hole
The start is always (0,0), and the goal is always (N-1, M-1).

A user can perform the following actions:
- Walk (left, right, up, down)
- Jump (over 1 hole)

For example, this course is Valid:
```
[[1, 0, 1],
 [0, 0, 1],
 [0, 0, 1]]
```

as the user can follow this path:
```
[[1 -> jump -> 1]
                    | walk
 [0        0      1]
                    | walk
 [0        0      1]
```

Given a N x M grid representing the course, return whether or not the course is valid.
这题不仅可以判断道路是不是通畅，还可以求出最少需要几步可以到目的地
注意clarify 1,1,1是不是可以跳跃，还是必须要一步一步走
这个对于能够到达没影响，因为1,1,1不管是一步一步走还是跳跃都能到
但是对于步数有影响，以下解法算步数是基于1,1,1可以跳跃的情况
'''
from collections import deque

class ObstacleCourses:
    # Time: O(n + m)
    # Space: O(n + m) ? 不太确定 一般bfs时间复杂度差不多就是空间复杂度
    def is_valid_course(self, courses: list[list[int]]) -> bool:
        n = len(courses)
        m = len(courses[0])
        if courses[0][0] != 1 or courses[n - 1][m - 1] != 1:
            return False

        one_steps = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        two_steps = [[0, -2], [-2, 0], [0, 2], [2, 0]]
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        steps = 0

        while queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()
                print(f'r: {row}, c: {col}')
                for d_r, d_c in one_steps:
                    new_r = row + d_r
                    new_c = col + d_c
                    print(f'nr1: {new_r}, nc1: {new_c}')
                    if new_r == n - 1 and new_c == m - 1:
                        print(steps + 1)
                        return True
                    if 0 <= new_r < n and 0 <= new_c < m and courses[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                
                for d_r, d_c in two_steps:
                    new_r = row + d_r
                    new_c = col + d_c
                    print(f'nr2: {new_r}, nc2: {new_c}')
                    if new_r == n - 1 and new_c == m - 1:
                        print(steps + 1)
                        return True
                    if 0 <= new_r < n and 0 <= new_c < m and courses[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            steps += 1
        
        return False

s = ObstacleCourses()
print(s.is_valid_course([[1, 0, 1],
                        [0, 0, 1],
                        [0, 0, 1]]))
