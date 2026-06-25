class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_list = [0]*3
        for i in nums:
            freq_list[i]+=1
        
        res = []
        for i in range(len(freq_list)):
            res.extend([i]*freq_list[i])
        

        for i in range(len(res)):
            nums[i]= res[i]

        # return res