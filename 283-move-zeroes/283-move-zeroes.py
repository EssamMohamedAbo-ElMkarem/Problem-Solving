class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp = nums.copy()
        n = len(nums)
        m = 0
        r = n - 1 
        for i in range(n):
            if cp[i]  == 0:
                nums[r] = 0
                r -= 1
            else:
                nums[m] = cp[i]
                m += 1
        return