class Solution:
    def quicksort(self, array):
        
        if len(array) < 2:
            return array
        pivot = array[0]
        left = [i for i in array[1:] if i <= pivot]
        right = [j for j in array[1:] if j > pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)
    
    
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            nums.append(target)
            nums = self.quicksort(nums)
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else: 
                high = mid - 1