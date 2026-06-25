class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0

        num_set = set(nums)
        d = {}
        for num in num_set:
            # print('num: ', num)
            is_checked = False
            if(len(d)==0):
                pass

            else:
                k = {i:j for i,j in d.items() if i<=num}
                sublists = [sublist for sublist in k.values()]
                is_checked = False
                for sublist in sublists:
                    # print(sublist, num)
                    if(num>=sublist[0] and num<=sublist[-1]):
                        # print(f'{num} is in {sublist}')
                        is_checked = True
                        break
            if(is_checked):
                continue

            num_elems = []
            for i in range(num, 10**9+1):
                if(i in num_set):
                    num_elems.append(i)
                else:
                    break
            if(len(num_elems)>0):
                d[num] = [num_elems[0], num_elems[-1]]
        

            # print('d: ', d)
            max_len = max([sublist[-1]-sublist[0]+1 for sublist in d.values()])
        return max_len