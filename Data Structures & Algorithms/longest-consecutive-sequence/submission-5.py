class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_list = sorted(set(nums))
        n = len(sorted_list)
        j = 1
        seq=[1]
        if nums: 
            for i in range(n-1):
                if sorted_list[i] + 1 == sorted_list[i+1] :
                    j+=1
                    seq.append(j)
                else:
                    j = 1
                    seq.append(j)
            return max(seq)