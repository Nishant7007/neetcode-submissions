class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mini = float('inf')
        while(l<=r):
            mid = (l+r)//2
            if(nums[l]<=nums[mid]):
                mini = min(mini, nums[l])
                l = mid+1
            else:
                mini = min(mini, nums[mid])
                r = mid-1
        return mini