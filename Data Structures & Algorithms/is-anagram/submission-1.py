class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt_s = {}
        cnt_t = {}

        for i in s:
            cnt_s[i] = cnt_s.get(i,0) + 1

        for j in t:
            cnt_t[j] = cnt_t.get(j,0) + 1

        for key in cnt_s:
            if key not in cnt_t:
                return False
            elif cnt_s[key] != cnt_t[key]:
                return False

        return True     