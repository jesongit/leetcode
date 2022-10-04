"""
854. 相似度为 K 的字符串
对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。

给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。



示例 1：

输入：s1 = "ab", s2 = "ba"
输出：1
示例 2：

输入：s1 = "abc", s2 = "bca"
输出：2


提示：

1 <= s1.length <= 20
s2.length == s1.length
s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
s2 是 s1 的一个字母异位词
"""
import time
# class Solution:
#     def kSimilarity(self, s1: str, s2: str) -> int:
#         """
#             既然这题都hard，直接交换铁超时，对吧，试试再说
#         """
#         cnt, i, maxi = 0, 0, len(s1)
#         s1 = list(s1)
#         while i < maxi:
#             if s1[i] == s2[i]:
#                 i += 1
#                 continue
#             j = s2.index(s1[i], i + 1)
#             s1[i], s1[j] = s1[j], s1[i]
#             cnt += 1
#         return cnt

# class Solution:
#     def kSimilarity(self, s1: str, s2: str) -> int:
#         """
#             尝试找到不是原来位置的交换，但是 Error 了 交换次数多了点
#             "abcdeabcdeabcdeabcde"
#             "aaaabbbbccccddddeeee"
#         """
#         cnt, i, maxi = 0, 0, len(s1)
#         s1 = list(s1)
#         while i < maxi:
#             if s1[i] == s2[i]:
#                 i += 1
#                 continue
#             j = i
#             while j == i or s1[j] == s2[j]:
#                 j = s2.index(s1[i], j + 1)
#             s1[i], s1[j] = s1[j], s1[i]
#             cnt += 1
#         return cnt


# class Solution:
#     def kSimilarity(self, s1: str, s2: str) -> int:
#         """
#             那就优先找能一次交换完成的 还是 Error 显然这题没这么简单
#             "aabbccddee"
#             "cdacbeebad"
#         """
#         cnt, i, maxi = 0, 0, len(s1)
#         s1 = list(s1)
#         while i < maxi:
#             if s1[i] == s2[i]:
#                 i += 1
#                 continue
#             for j in range(i, maxi):
#                 if s1[i] == s2[j] and s2[i] == s1[j]:
#                     s1[i], s1[j] = s1[j], s1[i]
#                     cnt += 1
#                     break
#             i += 1
#
#         while i < maxi:
#             if s1[i] == s2[i]:
#                 i += 1
#                 continue
#             j = i
#             while j == i or s1[j] == s2[j]:
#                 j = s2.index(s1[i], j + 1)
#             s1[i], s1[j] = s1[j], s1[i]
#             cnt += 1
#         return cnt

from queue import PriorityQueue


class Solution:

    def calc_distance(self, s1, s2):
        return (sum([0 if v == s2[i] else 1 for i, v in enumerate(s1)]) + 1) // 2

    def kSimilarity(self, s1: str, s2: str) -> int:
        """
            1. 因为以前写过一个类似棋盘的bfs + A* 算法，感觉这题很类似也想用类似的解法
            2. 但是还是遇到了一些问题，最后还是bfs+剪枝解题，看来答案后写下了 A* 的问题
            3. 从上面来看思路是没错的，但是漏了一些情况里面包含了最优解, 既然是最优解，优先还是选择 bfs
            4. 接下来先说说剪枝，这个比较重要
                4-1. s2[deep] == parent[i] != s2[i]
                    4-1-1. 第一个判断找到一个可以填到这个数字，第二个判断是剔除不需要移动的数字
                4-2. s2[i] == child[i] -> break
                    4-2-1. 这个是交换后，两边都可以不需要再移动，说明一定是这个格子的最优解之一，那就可以不管这个格子了
                4-3. 其实剪完支已经可以过了，A* 的问题当时没想明白
            5. 最开始设计的 A* 函数是 直接算一个有几个格子未复原的值
                5-1. sum([0 if v == s2[i] else 1 for i, v in enumerate(s1)])
                    5-1-1. 这里思路大致是没问题的，但是没考虑到前面走过的步骤，所有这个值的转化成步数 + 前面已经走过的步数
                5-2. (sum([0 if v == s2[i] else 1 for i, v in enumerate(s1)]) + 1) // 2 + step
                    5-2-1. 因为交换一次可以改变 2 个格子，那么完成的最小步数就需要把不同的值除 2，以及加上历史步数
        """

        maxi = len(s1)
        queue = PriorityQueue()
        queue.put((self.calc_distance(s1, s2), 0, 0, s1))
        # print(queue.get())

        while not queue.empty():
            pre_dis, step, deep, parent = queue.get()

            if parent[deep] == s2[deep]:
                if deep + 1 >= maxi:
                    # 匹配完了
                    return step

                # 已经一样了，找下一个的
                queue.put((pre_dis, step, deep + 1, parent))
                continue

            # 不一样，加入后面可以交换的所有情况
            for i in range(deep + 1, maxi):

                if s2[deep] == parent[i] != s2[i]:  # 可以交换的，并且原来不是匹配的字符 剪枝1

                    child = list(parent)
                    child[deep], child[i] = child[i], child[deep]
                    child = ''.join(child)

                    distance = self.calc_distance(child, s2)
                    if not distance:
                        return step + 1

                    if s2[i] == child[i]:
                        # 如果直接交换成功，那么一定是最优解，不需要考虑后面的了 剪枝2
                        queue.put((distance + step + 1, step + 1, deep + 1, child))
                        break

                    queue.put((distance + step + 1, step + 1, deep + 1, child))


if __name__ == '__main__':
    s1 = "aaaabbbbccccddddeeee"
    s2 = "bddceeceababeccddaab"

    st = time.time()
    solution = Solution()
    print(solution.kSimilarity(s1, s2))
    print(time.time() - st)
