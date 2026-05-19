from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        for num, fr in freq.items():
            buckets[fr].append(num)
        
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) != 0:
                for j in buckets[i]:
                    res.append(j)

                    if len(res) >= k:
                        return res
                