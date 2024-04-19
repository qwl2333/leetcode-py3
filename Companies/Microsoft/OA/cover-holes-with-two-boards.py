# There are N holes arranged in a row in the top of an old table. 
# We want to fix the table by covering the holes with two boards. 
# For technical reasons, the boards need to be of the same length. 
# The position of the K-th hole is A[K]. What is the shortest length of the boards required to cover all the holes? 
# The length of the boards has to be a positive integer. A board of length L, set at position X, covers all the holes located between positions X and X+L (inclusive). 
# The position of every hole is unique. Write a function: class Solution { public int solution(ini[] A); } 
# which, given an array A of integers of length N, representing the positions of the holes in the table, 
# returns the shortest board length required to cover all the holes.

# Examples: 
# 1. Given A=[11,20,15], your function should return 4. 
# The first board would cover the holes in positions 11 and 15 , and the second board the hole at position 20. 

# 2. Given A=[15,20,9,11], your function should return 5 . 
# The first board covers the holes at positions 9 and 11, and the second one the holes in positions 15 and 20

class Solution:
    # Time O(glogn + logn), space O(1)
    def find_shortest_board_to_cover_all_holes(self, positions_of_holes: list[int]) -> int:
        if len(positions_of_holes) <= 2:
            return 1
        positions_of_holes.sort()
        n = len(positions_of_holes)
        left_most = positions_of_holes[0]
        right_most = positions_of_holes[n - 1]
        target = (left_most + right_most) / 2

        l, r = 0, n - 1

        # find first element >= target, lower bound
        while l <= r:
            mid = (l + r) // 2
            if positions_of_holes[mid] >= target:
                r = mid - 1
            else: # positions_of_holes[mid] < target
                l = mid + 1
        
        if positions_of_holes[l] - target > target - positions_of_holes[l - 1]:
            return positions_of_holes[l - 1] - positions_of_holes[0]
        else:
            return positions_of_holes[n - 1] - positions_of_holes[l]

s = Solution()
print(s.find_shortest_board_to_cover_all_holes([1,11]))