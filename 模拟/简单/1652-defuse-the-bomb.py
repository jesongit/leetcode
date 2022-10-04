"""
1652. 拆炸弹
你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为 n 的 循环 数组 code 以及一个密钥 k 。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。

如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
如果 k == 0 ，将第 i 个数字用 0 替换。
由于 code 是循环的， code[n-1] 下一个元素是 code[0] ，且 code[0] 前一个元素是 code[n-1] 。

给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！



示例 1：

输入：code = [5,7,1,4], k = 3
输出：[12,10,16,13]
解释：每个数字都被接下来 3 个数字之和替换。解密后的密码为 [7+1+4, 1+4+5, 4+5+7, 5+7+1]。注意到数组是循环连接的。
示例 2：

输入：code = [1,2,3,4], k = 0
输出：[0,0,0,0]
解释：当 k 为 0 时，所有数字都被 0 替换。
示例 3：

输入：code = [2,4,9,3], k = -2
输出：[12,5,6,13]
解释：解密后的密码为 [3+9, 2+3, 4+2, 9+4] 。注意到数组是循环连接的。如果 k 是负数，那么和为 之前 的数字。


提示：

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
"""


class Solution:
    def decrypt(self, code, k):
        """
        没啥好说的模拟一下就行
        """
        max_len = len(code)
        if not k:
            return [0] * max_len

        # 这里算的是第一个位置的解密数字，以及 k 的正负当方向使用
        cursum, dir = 0, k // abs(k)
        for i in range(1, abs(k) + 1):
            index = (i * dir + max_len) % max_len
            cursum += code[index]

        ans, pre_inx, inx = [cursum] * max_len, 0, (dir + max_len) % max_len
        while inx:
            # 结果 = 上次和 - 自己数字 + 尾部数字
            tail = (inx + k + max_len) % max_len
            ans[inx] = ans[pre_inx] - code[inx] + code[tail]
            # print(inx, ans[pre_inx], code[inx], code[tail])
            pre_inx, inx = inx, (inx + dir + max_len) % max_len
        return ans


if __name__ == '__main__':
    solution = Solution()
    code = [5, 7, 1, 4]
    k = 3
    print(solution.decrypt(code, k))
