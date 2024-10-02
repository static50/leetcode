class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if ((num1 + num2) == target) and (index1 != index2):
                    return [index1, index2]
