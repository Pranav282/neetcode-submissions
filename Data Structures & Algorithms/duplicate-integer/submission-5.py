class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt_freq={}
        for i in nums:
            cnt_freq[i] = cnt_freq.get(i,0) + 1
            if cnt_freq[i] > 1:
                return True
        return False