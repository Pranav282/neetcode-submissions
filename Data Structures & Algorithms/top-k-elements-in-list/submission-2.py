class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num,0)+1 #create dictionary of count of char
        sorted_d = dict(sorted(cnt.items(), key=lambda x: x[1])) #sort dict based on the freq
        return list(sorted_d.keys())[-k:] #return keys for top k freq
        