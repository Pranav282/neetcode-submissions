class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt_s = {}
        for i in s:
            cnt_s[i] = cnt_s.get(i,0) + 1
        cnt_t = {}
        for i in t:
            cnt_t[i] = cnt_t.get(i,0) + 1
        for k in cnt_s:
            if cnt_s[k] != cnt_t.get(k, 0):
                return False

        return True