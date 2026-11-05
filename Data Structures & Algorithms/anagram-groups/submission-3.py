class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str=[]
        store_idx={}
        for word in strs:
            sorted_str = "".join(sorted(list(word)))
            if sorted_str not in store_idx:
                store_idx[sorted_str] = []

            store_idx[sorted_str].append(word)

        return list(store_idx.values())