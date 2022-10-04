"""
面试题 01.09. 字符串轮转
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

示例1:

 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
示例2:

 输入：s1 = "aa", s2 = "aba"
 输出：False
提示：

字符串长度在[0, 100000]范围内。
说明:

你能只调用一次检查子串的方法吗？
"""


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        """
        这里直接模拟了一下 比如 waterbottle 和 erbottlewat
        在 waterbottle 中找到 erbottlewat 的最后一个 t 的位置
        然后对比两端字符串即可  wat erbottle 和 erbottle wat
        然后因为第一个匹配的 t 不一定是正确的分段，所以要遍历完整个字符串
        """
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True
        i, max_len = 0, len(s1)
        for i, val in enumerate(s1):
            if s1[i] == s2[max_len - 1]:

                flag = True
                for j in range(max_len):
                    if j <= i and s1[j] != s2[max_len - i - 1 + j]:
                        flag = False
                        break
                    elif j > i and s1[j] != s2[j - i - 1]:
                        flag = False
                        break

                if flag:
                    return True

        return False


if __name__ == '__main__':
    pass
