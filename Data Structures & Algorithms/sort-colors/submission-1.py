class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for end in range(n-1, 0, -1):
            swapped = False
            for i in range(end):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True
            if not swapped:
                break
        return nums
        