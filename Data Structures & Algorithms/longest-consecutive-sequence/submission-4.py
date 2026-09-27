class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        set_nums = set(nums)
        max_seq = 1

        for num in set_nums:
            if num-1 not in set_nums:
                counter = 1
                while True:
                    if num+1 in set_nums:
                        counter += 1
                        num += 1
                    else:
                        break
                if counter > max_seq:
                    max_seq = counter
                counter = 0
        return max_seq