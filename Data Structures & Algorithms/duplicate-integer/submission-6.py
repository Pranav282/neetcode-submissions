class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt_dict={}
        for num in nums:
            cnt_dict[num] = cnt_dict.get(num,0) + 1
            if cnt_dict[num] > 1:
                return True
        return False