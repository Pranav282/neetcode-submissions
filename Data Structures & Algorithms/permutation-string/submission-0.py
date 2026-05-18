class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {} #count freq for string s1
        window_freq = {} #count freq for string s2
        s1_count = len ( set ( s1 ) ) #distinct count of characters in string

        for i in range( len( s1 ) ): #create hash map for frequency count
            s1_freq[ s1[ i ] ] = s1_freq.get( s1[ i ],0 ) + 1
        
        left = 0
        for right in range( len ( s2 ) ) : 
            window_freq[ s2[ right ] ] = window_freq.get( s2[ right ],0 ) + 1 #update frequency
            # maintain window size
            if right - left + 1 > len(s1):

                window_freq[s2[left]] -= 1

                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]

                left += 1

            # compare maps
            if window_freq == s1_freq:
                return True

        return False

                