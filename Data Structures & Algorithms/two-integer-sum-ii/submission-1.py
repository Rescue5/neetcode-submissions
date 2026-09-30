class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p2 > p1:
            n1, n2 = numbers[p1], numbers[p2]
            if n1+n2 == target:
                return [p1+1, p2+1]
            elif n1+n2 < target:
                p1+=1
                continue
            else:
                p2-=1
                continue
    
            
        