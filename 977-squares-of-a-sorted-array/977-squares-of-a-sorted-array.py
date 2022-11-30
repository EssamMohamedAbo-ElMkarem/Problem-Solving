class Solution:
    def quicksort(self, array):
       
        if len(array) < 2:
            return array
        pivot = array[0]
        left = [i for i in array[1:] if i <= pivot]
        right = [i for i in array[1:] if i > pivot]
        return self.quicksort(left) + [pivot] + self.quicksort(right)
    
    
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = []
        for i in nums:
            squares.append(i**2)
        return sorted(squares)
        