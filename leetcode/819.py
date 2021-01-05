import collections
import re
from typing import OrderedDict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_dic = {}
        sorted_dic = {}
        tmp = re.sub(pattern='\W', repl=' ', string=paragraph).lower().split()

        for s in tmp:
            if s not in banned:
                if s in word_dic:
                    word_dic[s] += 1
                else:
                    word_dic[s] = 1

        # value기준으로 딕셔너리 정렬
        sorted_dic = OrderedDict(sorted(word_dic.items(),
                                        key=lambda x: x[1],
                                        reverse=True))
        for k in sorted_dic.keys():
            return k
