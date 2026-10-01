class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                sm = nums[i] + nums[left] + nums[right]

                if sm == 0:
                    mid_res = [nums[i], nums[left], nums[right]]
                    if not mid_res in res:
                        res.append(mid_res)


                    left += 1
                    right -= 1
                
                elif sm < 0:
                    left+=1
                else:
                    right-=1
        return res