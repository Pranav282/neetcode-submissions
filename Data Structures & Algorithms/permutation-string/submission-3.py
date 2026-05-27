class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1 = len(s1)
        ns2 = len(s2)
        if ns2 < ns1:
            return False
        
        cnt_s1 = {}

        for i in range(ns1):
            cnt_s1[ s1[ i ] ] = cnt_s1.get(s1[ i ], 0 ) + 1

        cnt_s2 = {}
        j = 0
        for i in range(ns2): 
            cnt_s2[ s2[ i ] ] = cnt_s2.get(s2[ i ], 0 ) + 1

            while cnt_s2.get(s2[i],0) > cnt_s1.get(s2[i],0):

                cnt_s2[s2[j]] -= 1

                if cnt_s2[s2[j]] == 0:
                    del cnt_s2[s2[j]]

                j += 1

            if (i - j + 1) == ns1 and cnt_s1 == cnt_s2:
                return True
        return False
