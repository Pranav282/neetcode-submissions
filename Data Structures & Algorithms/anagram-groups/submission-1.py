class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_cnt = {}
        output=[]
        for i, word in enumerate ( strs ):
            new_wrd = str("".join(sorted(word)))
            if new_wrd not in dict_cnt:
                dict_cnt[new_wrd]=[]
            dict_cnt[new_wrd].append(word)
        for value in dict_cnt.values():
            output.append(value)
        return output