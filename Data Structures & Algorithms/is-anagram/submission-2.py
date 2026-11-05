class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = {}
        cnt_t= {}
        for i in s:
            cnt_s[i] = cnt_s.get(i,0) + 1 
        for j in t:
            cnt_t[j] = cnt_t.get(j,0) + 1
        return cnt_s == cnt_t