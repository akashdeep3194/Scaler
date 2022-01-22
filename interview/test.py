# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
# is that adjacent houses have security system connected and it will automatically contact the police if two
# adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police

# Input: nums = [1,2,3,1]  -> (3,False) (3,True)
# Output: 4

def solve(nums):
    return max(maxMoney(nums))


def maxMoney(nums):

    if len(nums) == 1:
        return [0, nums[0]]

    sa = maxMoney(nums[1:])

    amt_excluding_ele = sa[0]
    amt_including_ele = sa[1]

    amt_0 = amt_excluding_ele+nums[0]
    amt_1 = max(amt_including_ele, amt_excluding_ele)

    return [amt_1, amt_0]


nums = [2, 1, 1, 2, 5, 6]

print(solve(nums))
# print(maxMoney([1, 1, 2]))
