class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs={}

        for string in strs:
            sorted_str = "".join(sorted( list(string) ) )
            
            if sorted_str not in sorted_strs:
                sorted_strs[sorted_str] = []
            sorted_strs[sorted_str].append(string)

        return list(sorted_strs.values())