"""
817. 链表组件
给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。

返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。



示例 1：
[img]https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom1.jpg[/img]

输入: head = [0,1,2,3], nums = [0,1,3]
输出: 2
解释: 链表中,0 和 1 是相连接的，且 nums 中不包含 2，所以 [0, 1] 是 nums 的一个组件，同理 [3] 也是一个组件，故返回 2。
示例 2：
[img]https://assets.leetcode.com/uploads/2021/07/22/lc-linkedlistcom2.jpg[/img]

输入: head = [0,1,2,3,4], nums = [0,3,1,4]
输出: 2
解释: 链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。


提示：

链表中节点数为n
1 <= n <= 104
0 <= Node.val < n
Node.val 中所有值 不同
1 <= nums.length <= n
0 <= nums[i] < n
nums 中所有值 不同
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        """
        模拟遍历一遍，看看哪里断开的就行，官方题解用 set 来处理 in_list 更快，但是这样也过了就没改
        """
        cnt, flag = 0, False
        while head is not None:

            index = nums.index(head.val) if head.val in nums else None
            if index is not None:
                cnt += 1 if not flag else 0
                nums.pop(index)
                flag = True
            else:
                flag = False
            head = head.next
        return cnt


if __name__ == '__main__':
    node = None
    for i in range(5, -1, -1):
        node = ListNode(i, node)

    list = [0, 3, 1, 4]

    solution = Solution()
    print(solution.numComponents(node, list))
