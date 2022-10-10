"""
801. 使序列递增的最小交换次数
我们有两个长度相等且不为空的整型数组 nums1 和 nums2 。在一次操作中，我们可以交换 nums1[i] 和 nums2[i]的元素。

例如，如果 nums1 = [1,2,3,8] ， nums2 =[5,6,7,4] ，你可以交换 i = 3 处的元素，得到 nums1 =[1,2,3,4] 和 nums2 =[5,6,7,8] 。
返回 使 nums1 和 nums2 严格递增 所需操作的最小次数 。

数组 arr 严格递增 且  arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1] 。

注意：

用例保证可以实现操作。


示例 1:

输入: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
示例 2:

输入: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
输出: 1


提示:

2 <= nums1.length <= 105
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 2 * 105
"""


class Solution:
    """
    典型的动态规划吧方便理解定义一个二维数组可以，想到这个思路，感觉没有 hard 难度
    dp[i][j] i 数组对应下标，j 表示是否交换 0不交换，1交换
    *因为只关心当前的 i 是否需要交换，所以只需要判断 与i-1 位置数字的大小即可*

    1. 首先是都满足的情况下 如 [1,3] [2,4] 对应下标都是  i-1 和 i
        不管怎么交换都是满足要求的，所以直接取最小值就行了
        dp[i][0] = min(dp[i-1][0], dp[i-1][1])
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
    2. 然后是只有不交换才能满足要求的 [1,2] [3,4]
        只能同时不交换或者同时交换才能满足要求
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1] + 1
    3. 只有交换才能满足要求 [1,4],[3,2]
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1] + 1
    4. 这里其实已经递推完了，但是还有一点，就是当 nums1[i] == nums2[i] 时候
        这时候交换是没有意义的，所以当他们相等时并且 j == 1 时候，不应该加 1
    5. 然后就是当前 i 只和 i-1 有关系，之前的数据就没用了，就可以优化一下空间
        add0, add1 表示上次不交换和交换的最小次数直接递推这次的就行了
    """

    def minSwap(self, nums1, nums2):
        max_len = len(nums1)
        add0, add1 = 0, 0 if nums1[0] == nums2[0] else 1

        for i in range(1, max_len):
            add = 0 if nums1[i] == nums2[i] else 1

            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1] and \
                    nums2[i] > nums1[i - 1] and nums1[i] > nums2[i - 1]:
                # 情况1
                add0, add1 = min(add1, add0), min(add0, add1) + add
            elif nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                # 情况2
                add0, add1 = add0, add1 + add
            else:
                # 情况3
                add0, add1 = add1, add0 + add
        return min(add0, add1)


if __name__ == '__main__':
    # list1 = [0, 4, 4, 5, 9]
    # list2 = [0, 1, 6, 8, 10]
    # list1 = [0, 1, 4, 6, 8]
    # list2 = [1, 2, 2, 7, 10]
    # list1 = [0, 7, 8, 10, 10, 11, 12, 13, 19, 18]
    # list2 = [4, 4, 5, 7, 11, 14, 15, 16, 17, 20]
    list1 = [0, 4, 4, 5, 9]
    list2 = [0, 1, 6, 8, 10]
    solution = Solution()
    print(solution.minSwap(list1, list2))
