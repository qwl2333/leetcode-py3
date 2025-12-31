# lc 295 和 lc 480类似, 当480是进阶版, 加了prune 为了延迟删除

# 在 Python 的 heapq 模块中，heappush 和 heappop 的时间复杂度都是 O(log N)。
# 以下是详细的拆解和原因：
# 为什么是 O(log N)？Python 的 heapq 是基于二叉堆 (Binary Heap) 实现的（具体是一个完全二叉树）：
#
# heappush(heap, item): 它首先把新元素放在堆的末尾（树的最后一个叶子节点），然后执行“上浮”操作（Sift-up），
# 将这个元素与其父节点比较并交换，直到满足堆特性。在一个有 N 个节点的完全二叉树中，树的高度是 log_2 N，
# 所以最多只需要交换 log N 次。
#
# heappop(heap): 它弹出堆顶元素（根节点，最小的值）。为了保持完全二叉树的形状，它把最后一个元素挪到堆顶，
# 然后执行“下沉”操作（Sift-down），将这个新的堆顶元素与子节点比较并交换，直到满足堆特性。同理，这最多也只需要沿着树的高度走 log N 步。

from heapq import heappush, heappop
class MedianFinder:
    '''
    N的含义: 到目前为止, 你通过 addNum 总共存入的数字个数

    TC:
    addNum O(logN) 包含两次主要操作: 1. 插入堆 (heappush) 耗时 O(log N)
                                  2. 平衡堆 (pop + push) 耗时 O(log N)。N 是当前数据流中的元素总数。
    findMedian O(1) 只需要查看堆顶元素 (self.small[0] 或 self.large[0])

    SC: O(N) 你需要存储数据流中出现过的所有数字, self.small 存储约 N/2 个元素, self.large 存储约 N/2 个元素
    '''
    def __init__(self):
        self.small = [] # maxheap store -(num)  small has smaller part of the stream, small returns largest
        self.large = [] # minheap store (num)  large has bigger part of the stream, large returns smallest so we can get median
        # [1,2,3,4,5,6,7]
        # low:  4,3,2,1
        # high: 5,6,7

    def addNum(self, num: int) -> None:
        if not self.small:
            heappush(self.small, -num)
            return

        if num > -self.small[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)

        # 核心规则
        # 添加数字：
        # 如果新数字比左边最大的还小，就扔进左边的 small。
        # 否则，扔进右边的 large。
        # 重新平衡 (Rebalance)：
        # 左边太多了（small_size > large_size + 1）：把左边最大的（堆顶）踢到右边去。
        # 右边太多了（large_size > small_size）：把右边最小的（堆顶）踢到左边去。
        if len(self.small) - len(self.large) > 1: # len(low) 要么和 len(high) 相等，要么多一个，否则就要rebalance
            heappush(self.large, -self.small[0])
            heappop(self.small)
        elif len(self.large) - len(self.small) > 0:
            heappush(self.small, -self.large[0])
            heappop(self.large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

sol = MedianFinder()
sol.addNum(2)
sol.addNum(2)
sol.addNum(3)
sol.addNum(3)
print(sol.findMedian())