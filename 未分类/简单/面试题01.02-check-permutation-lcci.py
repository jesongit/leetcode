"""
面试题 01.02. 判定是否互为字符重排
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        统计每个字符的个数，再对比一遍即可
        """
        if len(s1) != len(s2):
            return False
        dict = {}
        for c in s1:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for c in s2:
            if c not in dict:
                return False

            if dict[c] == 1:
                dict.pop(c)
            else:
                dict[c] -= 1
        return not dict


if __name__ == '__main__':
    """
    "bkhfhqlayvlhdqmxvnkqvtkojouugfsnwmyoywkilsnubnkvhdbrltuxvoblurpfinpigajttcvkcxlylblcaocsjmwdvwepvnfr"
    "mtycyvobjldulmhsuqvtrhqnisjkuxhvaxqkvpbllnkvvakxjbolefpyrtiivvwctunasbbocldflkcknmwgofngorduwlwhyfnp"
    """
    s1 = "bkhfhqlayvlhdqmxvnkqvtkojouugfsnwmyoywkilsnubnkvhdbrltuxvoblurpfinpigajttcvkcxlylblcaocsjmwdvwepvnfr"
    s2 = "mtycyvobjldulmhsuqvtrhqnisjkuxhvaxqkvpbllnkvvakxjbolefpyrtiivvwctunasbbocldflkcknmwgofngorduwlwhyfnp"
    solution = Solution()
    print(solution.CheckPermutation(s1, s2))
    pass
