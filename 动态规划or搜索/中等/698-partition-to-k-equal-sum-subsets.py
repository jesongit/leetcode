"""
698. 划分为k个相等的子集
给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
示例 2:

输入: nums = [1,2,3,4], k = 3
输出: false

提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000
每个元素的频率在 [1,4] 范围内

link: https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
"""
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
            状态压缩的动态规划，可以理解为一个bfs
            1. 这里的状态是对应每个数字是否被使用，所以只有2个状态，可以进行状态压缩使用0和1表示
            2. sums[0] 表示还没填数，一定是可行的，然后往后递推，0表示当前状态，对应的值是对应数字和取余平均数
            3. 这里有个重要的点就是取余，取余的原因是快速计算出当前集合中最大的可用空间
                3-1. 假设有一个上限为平均数的桶，这里的方式就是不断往里面装
                    3-1-1. 当然可以理解为 k 个桶，但是只能一个一个装，道理是一样的
                3-2. 然后没装满就继续装，装满了就倒掉继续装，但是不能溢出
                3-3. 这里取余的作用就是这个，当然可以可以换成满了就清空
            4. 所以本质上就是一个bfs，遍历了所有可能的情况，只不过忽略了k个桶这个参数
        """
        ans = sum(nums)
        if ans % k:
            return False

        avg = ans // k
        nums.sort()
        if nums[-1] > avg:
            return False

        n = len(nums)
        n2 = 1 << n

        dp = [False] * n2   # 记录当前数字集合的可行性
        sums = [0] * n2     # 当前数字集合取余平均数的结果
        dp[0] = True        # 设置一个可行的起点

        for i in range(n2):
            if not dp[i]:
                # 已经判断了不可行，就不用往下走了
                continue
            for j in range(n):
                # 寻找可以填的数字
                num = sums[i] + nums[j]
                if num > avg:
                    # 最大空间都填不下当前数，后面就不用填了
                    break
                if i >> j & 1 == 0:
                    # 当前数没使用过，计算使用了的状态集合
                    inx = i | (1 << j)
                    if not dp[inx]:
                        # 如果是可行就不用判断了
                        sums[inx] = 0 if num == avg else num
                        # sums[inx] = (sums[i] + nums[j]) % avg
                        dp[inx] = True

        return dp[n2 - 1]
