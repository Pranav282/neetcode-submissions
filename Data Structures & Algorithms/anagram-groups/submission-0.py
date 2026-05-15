class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_map = {}

        for s in strs:
            sorted_str = ''.join(sorted(s)) #sort each string 

            if sorted_str not in dict_map:
                dict_map[sorted_str] = [] #if not in dict create an empty list as value

            dict_map[sorted_str].append(s) #append original string to list

        final_list = []

        for v in dict_map.values():
            final_list.append(v) #create a list of all the grouped anagrams

        return final_list