class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        pos = 0
        for i,num in enumerate(nums):
            if num == val:
                continue
            else: 
                nums[pos]=nums[i]
                pos=pos+1
                k=k+1
        return k