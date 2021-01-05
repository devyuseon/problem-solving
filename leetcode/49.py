import re


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for word in strs:
            strs.remove(word)
            tmp = [word]
            word_list = ','.join(word).split(',')
            word_list.sort()
            for s in strs:
                s_list = ','.join(word).split(',')
                s_list.sort()
                if word_list == s_list:
                    tmp.append(s)
                    strs.remove(s)
            anagrams.append(tmp)
        return anagrams
