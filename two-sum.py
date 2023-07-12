class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for j in range(len(nums)):
            curr = nums[j]
            if target - curr in dic and j != dic[target-curr]:
                return [j, dic[target-curr]]