from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []

        # 'to' 기준으로 어휘순 정렬 (오름차순)
        tickets.sort(key= lambda x: x[1])

        # 'JFK' 출발인 티켓 인덱스 구함 (정렬되어있어 최초 등장 구함)
        index = 0
        for i, ticket in enumerate(tickets):
            if tickets[0] == 'JFK':
                index = i
                break
        tmp = tickets[index]
        tickets.remove(tickets[index])

        dic = collections.OrderedDict(tickets)
        dfs()

        return tickets