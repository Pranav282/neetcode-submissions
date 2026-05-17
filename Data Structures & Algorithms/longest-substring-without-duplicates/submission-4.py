class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_count = {} #dictionary map to count frequency
        i = 0 #left pointer
        max_length = 0 #max length 

        for j in range(len(s)): #loop though right pointer

            # add current character
            char_count[s[j]] = char_count.get(s[j], 0) + 1 #increase freq

            # if duplicate exists, shrink window until duplicate is found and count decreased
            while char_count[s[j]] > 1: 

                char_count[s[i]] -= 1
                i += 1

            # update answer
            max_length = max(max_length, j - i + 1)

        return max_length