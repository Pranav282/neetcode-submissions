class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        if len(nums) == 1 or len(nums) == 0:
            return False
        for i in range(len(nums)):
            cnt[nums[i]] = cnt.get(nums[i],0) + 1
            if cnt[nums[i]] > 1:
                return True
                break
            elif i == len(nums) - 1:
                return False
