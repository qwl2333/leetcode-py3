#
# Complete the 'suitableLocations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY center
#  2. LONG_INTEGER d
#
from collections import defaultdict
def suitableLocations(center, d):
    # Write your code here
    # sort center
    # min(center) +d, max(center) - d
    
    center.sort()
    freq = defaultdict(int)
    for c in center:
        freq[c] = freq[c] + 1
        
    n = len(center)
    min_c = center[0]
    max_c = center[n - 1]
    half_d = d // 2
    left = min(min_c + half_d, max_c - half_d)
    right = max(min_c + half_d, max_c - half_d)
    new_len = right - left + 1
    res = []
    left_c = [0 for i in range(new_len)]
    right_c = [0 for i in range(new_len)]
    
    for i in range(1, new_len):
        left_b = left_c + i
        print(left_b)
        if left_b in freq:
            left_c[i] = left_c[i - 1] + freq[left + i]
        else:
            left_c[i] = left_c[i - 1]
    
    print(freq)
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    center_count = int(input().strip())

    center = []

    for _ in range(center_count):
        center_item = int(input().strip())
        center.append(center_item)

    d = int(input().strip())

    result = suitableLocations(center, d)

    fptr.write(str(result) + '\n')

    fptr.close()
