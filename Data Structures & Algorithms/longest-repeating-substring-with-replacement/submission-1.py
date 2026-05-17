class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s) #length of string
        freq={} #freq map
        l=0 #left pointer
        max_length=0
        max_freq = 0
        for r in range(n): #start right pointer
            freq[s[r]]=freq.get(s[r],0)+1
            max_freq = max(max_freq, freq[s[r]])
            current_length = ( r - l + 1)
            while ( current_length -max_freq  ) > k:
                freq[s[l]]-=1
                l+=1
                current_length = ( r - l + 1)
            max_length = max(max_length,current_length)
                
        return max_length