"""
面试题 17.19. 消失的两个数字
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]
示例 2:

输入: [2,3]
输出: [1,4]
提示：

nums.length <= 30000
"""
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        """
        很遗憾，这题没写出来，虽然也想到了位运算之类的，但是也不知道怎么解
        另外非官方题解中有一个更好理解的方式，这里就使用他的方式解题
        """

        # 算出和之差，即 x + y = ?
        max_len = len(nums) + 2
        max_sum = ((1 + max_len) * max_len) >> 1
        dif_sum = max_sum - sum(nums)

        # 算出平均数以及，正常情况下到平均数的和
        dif_avg = dif_sum >> 1
        max_sum = ((1 + dif_avg) * dif_avg) >> 1

        cur_sum = 0
        for num in nums:
            if num <= dif_avg:
                cur_sum += num

        # 正常的和 - 残缺数组中到平均数的和 = 小点的数
        min_num = max_sum - cur_sum
        max_num = dif_sum - min_num
        return [min_num, max_num]


if __name__ == '__main__':
    pass
