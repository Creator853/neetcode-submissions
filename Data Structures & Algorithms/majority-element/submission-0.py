class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen: dict[int, int] = {}
        majority_element = 0
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        for key,value in seen.items():
            if value > len(nums)//2:
                majority_element = key
        return majority_element
                
        