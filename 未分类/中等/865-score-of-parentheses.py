"""
856. 括号的分数
给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

() 得 1 分。
AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
(A) 得 2 * A 分，其中 A 是平衡括号字符串。


示例 1：

输入： "()"
输出： 1
示例 2：

输入： "(())"
输出： 2
示例 3：

输入： "()()"
输出： 2
示例 4：

输入： "(()(()))"
输出： 6


提示：

S 是平衡括号字符串，且只含有 ( 和 ) 。
2 <= S.length <= 50
"""


class Solution:
    """
    官方提交提供了3种解法，包括分治、栈和深度来计算值
    感觉我的解法和哪个都不太像，栈的解法有思考过但没使用，最优解法应该是用深度的方式算出来

    感觉我写的更像模拟？
    """
    def calc(self, s, inx):
        # '()' 1分
        if s[inx + 1] == ')':
            return 1, inx + 2

        # 'AB' 的情况 加起来
        tmp, tail = self.calc(s, inx + 1)
        while s[tail] != ')':
            add, tail = self.calc(s, tail)
            tmp += add

        # 传进来的inx 一定有个 '(' 那么就有 ')' 需要 *2
        return tmp * 2, tail + 1

    def scoreOfParentheses(self, s: str) -> int:
        """
        应该有更好的写法，不过我好懒-_-!
        """
        tmp, tail = self.calc(s, 0)
        # calc 只能算 一个闭合 (XXXXX) 括号类的情况， 存在 '(XX)(XX)' 需要累加
        while tail < len(s) and s[tail] == '(':
            add, tail = self.calc(s, tail)
            tmp += add
        return tmp


if __name__ == '__main__':
    # s = '(()(()))'
    s = '(())()'
    solution = Solution()
    print(solution.scoreOfParentheses(s))
