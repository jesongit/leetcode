"""
769. 最多能完成排序的块
给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。

我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。



示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。


提示:

n == arr.length
1 <= n <= 10
0 <= arr[i] < n
arr 中每个元素都 不同
"""
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        直接模拟过了，官方题解貌似没那么好理解。。。
        """
        cnt, nmin, nmax, nlen = 0, len(arr), -1, 0
        for i, num in enumerate(arr):

            nlen += 1
            nmin = min(nmin, num)
            nmax = max(nmax, num)
            # print(i, nlen, nmin, nmax)

            if nmax - nmin + 1 == nlen and i == nmax:
                # 如果分块是合理的
                # 1. 那么分块的最大值 - 最小值 + 1 一定等于分块长度，只要这样排序后才是连续的序列
                # 2. 第一点只能保证分块是连续的，无法保证位置是对的，
                #   2.1 比如 4，3 排序后也是连续的, 但是不能在 0, 1 的位置
                #   2.2 所以还要多判断一个 当前下标需要等于最大值，
                cnt, nmin, nmax, nlen = cnt + 1, len(arr), -1, 0

        return cnt


if __name__ == '__main__':
    list = [4, 3, 2, 1, 0]
    # list = [1, 0, 2, 3, 4]
    # list = [0, 3, 4, 1, 2]
    solution = Solution()
    print(solution.maxChunksToSorted(list))
