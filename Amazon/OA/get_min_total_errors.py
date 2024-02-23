class Solution:
# Databases doesn't support very large numbers, so numbers are stored as a string of binary characters, '0' and '1. Accidentally, a ! was entered at some positions and it is unknown whether they should be '0' or ‘1’.
# The string of incorrect data is made up of the characters '0, 1' and ! where !' is the character that got entered incorrectly. '!' can be replaced with either '0' or '1'. Due to some internal faults, some errors are generated every time '0' and '1' occur together as '01' or 10 'in any subsequence of the string. It is observed that the number of errors a subsequence '01' generates is x, while a subsequence '10' generates y errors.

# Determine the minimum total errors generated? Since the answer can be very large, return it modulo 10^9+7.
# For example, given string errorString ="101!1", x = 2, y = 3

# If the '! at index 3 is replaced with '0, the string is "10101". The number of times the subsequence 01 occurs is 3 at indices (1, 2), (1, 4), and (3,4). The number of times the subsequence 10 occurs is also 3, indices (0, 1), (0, 3) and (2, 3). The number of errors is 3 * x+3 * y=6 + 9 = 15.
# If the ! is replaced with '1, the string is "10111". The subsequence 01 occurs 3 times and 10 occurs 1 time. The number of errors is 3 * x + y = 9.
# The minimum number of errors is min(9, 15) modulo (10^9 +7) = 9.
    
    def get_min_total_errors(self, error_string: str, x: int, y: int) -> int:
        n = len(error_string)
        left_one_count = [0 for _ in range(n + 1)]
        left_zero_count = [0 for _ in range(n + 1)]

        zero_counter = 0
        one_counter = 0
        for i in range(1, n + 1):
            if error_string[i - 1] == '0':
                zero_counter += 1
            else:
                one_counter += 1
            left_one_count[i] = one_counter
            left_zero_count[i] = zero_counter
        print(left_one_count)
        print(left_zero_count)
        one_zero_sub_count = 0
        zero_one_sub_count = 0
        for i in range(n):
            if error_string[i] == '1':
                zero_one_sub_count += left_zero_count[i]
            else:
                one_zero_sub_count += left_one_count[i]
        
        return zero_one_sub_count * x + one_zero_sub_count * y
        

s = Solution()
input_error_string = '101!1'
DIVISOR = 10 ** 9 + 7 # 除数（分子） divisor， 被除数（分母） dividend
idx = input_error_string.find('!')
replaced_by_one = input_error_string[:idx] + '0' + input_error_string[idx+1:]
replaced_by_zero = input_error_string[:idx] + '1' + input_error_string[idx+1:]
result1 = s.get_min_total_errors(replaced_by_zero, 2, 3)
result2 = s.get_min_total_errors(replaced_by_one, 2, 3)
res = min(result1, result2) % DIVISOR
print(res)
