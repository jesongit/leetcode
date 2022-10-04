"""
面试题 17.09. 第 k 个数
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9
"""


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        """
        当然可以直接打表。。。。所谓dp或者3指针，看怎么好理解就怎么想
        """
        dp = [1]
        i, p1, p2, p3 = len(dp), 0, 0, 0
        while i < k:
            # print(dp, p1, p2, p3)
            dp.append(min(dp[p1] * 3, dp[p2] * 5, dp[p3] * 7))
            p1 += 1 if dp[i] == dp[p1] * 3 else 0
            p2 += 1 if dp[i] == dp[p2] * 5 else 0
            p3 += 1 if dp[i] == dp[p3] * 7 else 0
            i += 1
        return dp[k - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.getKthMagicNumber(7))
    pass
