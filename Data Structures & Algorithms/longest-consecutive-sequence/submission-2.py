class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if len(nums) == 0:
            return 0
        
        max_seq = 1

        for num in num_set:
            if (not num-1 in num_set and num+1 in num_set):
                current_seq = 1
                while num+1 in num_set:
                    current_seq += 1
                    num +=1
                if current_seq > max_seq:
                    max_seq = current_seq
        return max_seq
            

