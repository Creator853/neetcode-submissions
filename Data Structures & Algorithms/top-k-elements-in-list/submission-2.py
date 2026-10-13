
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Create frequency map
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] = seen[num] + 1
            else:
                seen[num] = 1

        # Step 2: Create buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # Step 3: Place each number in its frequency bucket
        for num in seen:
            frequency = seen[num]
            buckets[frequency].append(num)

        # Step 4: Collect k most frequent numbers
        result = []

        for frequency in range(len(nums), 0, -1):
            for num in buckets[frequency]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
