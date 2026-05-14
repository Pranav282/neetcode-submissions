class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for index, val in enumerate(nums):
            complement = target - val
            if complement in seen_map:
                # We found the pair!
                return [seen_map[complement], index]
            seen_map[val] = index