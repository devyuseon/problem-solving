from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = []
    sorted_words = []
    for word in strs:
        sorted_words.append(sorted(','.join(word).split(',')))
    for i in range(len(strs)):
        if strs[i] != None:
            tmp = [strs[i]]
            strs[i] = None
            for j in range(i+1, len(strs)):
                if sorted_words[i] == sorted_words[j]:
                    tmp.append(strs[j])
                    strs[j] = None
            anagrams.append(tmp)
    return anagrams
