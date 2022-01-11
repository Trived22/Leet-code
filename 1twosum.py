class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,curval in enumerate(nums) :
            sub = target - curval
            if sub in a:
                return [a[sub],i]
            else :
                a[curval] = i
            class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,curval in enumerate(nums) :
            sub = target - curval
            if sub in a:
                return [a[sub],i]
            else :
                a[curval] = i
            
