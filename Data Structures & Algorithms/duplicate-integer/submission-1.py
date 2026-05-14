class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i, num in enumerate(nums):
            cnt[num]=cnt.get(num,0) + 1
            if cnt[num] > 1:
                return True
                break
        return False