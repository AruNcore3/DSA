from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int)-> List[int]:
        h_tble:dict[int,int] = Counter(nums)
        res:list[int] = []
        for _ in range(k):
            m = max(h_tble,key=h_tble.get)
            res.append(m)
            h_tble.pop(m)
        return res

            




        