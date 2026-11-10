class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        cnt_s = {}
        cnt_t= {}

        if len_s != len_t:
            return False


        for i in range(len_s):
            cnt_s[s[i]] = cnt_s.get(s[i], 0) + 1
            cnt_t[t[i]] = cnt_t.get(t[i], 0) + 1

        return cnt_s == cnt_t