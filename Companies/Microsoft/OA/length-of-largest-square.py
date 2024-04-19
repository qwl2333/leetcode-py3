# M 个 1 * 1 tiles, N 个 1 * 1 tiles, return the length of the largest square created using these tiles
from math import floor, sqrt

class Solution:
    def get_length_of_largest_square(self, m: int, n: int) -> int:
        sum_area = m + n * 4
        length_limit = floor(sqrt(sum_area))
        for i in range(length_limit, -1, -1):
            max_num_of_two_at_one_side = i // 2
            max_num_of_two_needed = max_num_of_two_at_one_side ** 2
            area_for_two = 4 * max_num_of_two_needed if n >= max_num_of_two_needed else 4 * n
            area_for_one = i ** 2 - area_for_two
            if m >= area_for_one:
                return i

        return 0

    # https://www.geeksforgeeks.org/maximum-square-side-length-with-m-1x1-and-n-2x2-tiles/
    # We can not build a square having length greater than sqrt(4*n+m).

    # Let x=sqrt(4*n+m).

    # if x is even then the whole x by x grid can be divide into 2 by 2 squares. So we will use the maximum possible 2 by 2 squares and since 4*n+m>=x*x so simply x is the answer.

    # if x is odd then the maximum possible 2 by 2 squares that can be used is ((x-1)*(x-1))/4; Let val1=((x-1)*(x-1))/4.

    # So 2 by 2 squares used will be min(val1,n); now if 4*min(val1,n)+m>=x*x then x is answer otherwise x-1 is the answer.
    def findTiles(self, M, N):
        x = floor(sqrt(4 * N + M))
        if x % 2 == 0:
            return x
        else:
            inter = ((x - 1) * (x - 1)) // 4
            if 4 * min(inter, N) + M >= x * x:
                return x
            else:
                return x - 1

s = Solution()
print(s.findTiles(1, 2))