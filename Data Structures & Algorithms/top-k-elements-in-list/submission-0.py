class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            if(i in freq_dict):
                freq_dict[i]+=1
            else:
                freq_dict[i]=1

        freq_count_dict = {i:[] for i in range(1, len(nums)+1)}
        for i, j in freq_dict.items():
            freq_count_dict[j].append(i)
        
        # print(freq_count_dict)
        
        res = []
        for i in range(len(nums), 0, -1):
            if(len(freq_count_dict[i])>0):
                k-=len(freq_count_dict[i])
                res.extend(freq_count_dict[i])
            if(k<1):
                return res
        
        return res
