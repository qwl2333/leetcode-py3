# lc 239
import collections
class Solution(object):
    # O(n)
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque() # 维护一个非严格的递减的deque, [2,1,1]允许,[3,2,1]允许，[1,2]不允许
        # 每次d[0]就是window内最大的数的idx，注意deque里面存的是index
        # 仔细思考，当我们在循环便利这个nums时, d表示的是在当前window[i-k, i - 1]，这k个值面对即将加入的i，需要做什么
        # 1 维持d的非严格的递减
        # 2 加入i
        # 3 维护d没有超过size
        # 4 把最大的d[0]放入结果
        out = []
        for i, n in enumerate(nums):
            print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
            while d and nums[d[-1]] < n: # 在存当前的idx i之前，需要确保deque里面从最小(左)开始没有比当前值更小的（可以相等，
                                        # 如果有就要pop出来，有更小的意味着更小的是无效的值
                                        # 为方便展示用值而不是idx在deque里面， 比如[4,2,1],此时是3，3肯定比1，2大，意味着window里面的1,2其实已经无效了
                                        # 因为即将加入的3肯定会让1,2无效，再也不可能被放到结果里面去
                d.pop()
                print("\t Popped from d because d has elements and nums[d.top] < curr element")
            d.append(i)
            print("\t Added i to d")
            if d[0] == i - k: # 存idx的好处，方便计算左边的边界i-k是不是已经到了，到了就需要把它从d里面pop出来
                d.popleft()
                print("\t Popped left from d because it's outside the window's leftmost (i-k)")
            if i >= k-1: # 只有i到达k-1开始才需要把最大的数的idx存到结果里去
                out.append(nums[d[0]])
                print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
        return out

s = Solution()
print(s.maxSlidingWindow([1,1,1,-3,5,3,6,7], 3))