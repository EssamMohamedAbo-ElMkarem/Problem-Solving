class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tempsum = 0
        newArr = []
        for i in range(len(nums)):
            for j in range(i+1):
                tempsum += nums[j]
            newArr.append(tempsum)
            tempsum = 0
        return newArr