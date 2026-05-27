class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = {}
        n = len(s)
        i = 0

        max_length = 0
        current_length=0
        for j in range(len(s)):

            cnt[s[j]] = cnt.get(s[j], 0) + 1

            while cnt[s[j]] > 1:

                cnt[s[i]] -= 1
                i += 1
            max_length=max(max_length, j-i+1)

        return max_length  