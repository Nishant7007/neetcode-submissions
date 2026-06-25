from collections import Counter
class Solution:        
        # def minWindow(self, s: str, t: str) -> str:
        #     if(s==t):
        #         return s
        #     if(len(t)>len(s)):
        #         return ''
        #     count_t = Counter(t)
        #     count_s = Counter(s)
        #     l=0
        #     r=len(s)-1
        #     min_len = len(s)
        #     while(l<=r):
        #         print(s[l:r+1])
        #         l_element = s[l]
        #         r_element = s[r]
        #         if((l_element not in count_t) or (count_s[l_element]>count_t[l_element])):
        #             l+=1
        #             min_len-=1
        #             count_s[l_element]-=1
        #             res = s[l:r+1]
        #         elif((r_element not in count_t) or (count_s[r_element]>count_t[r_element])):
        #             r-=1
        #             min_len-=1
        #             count_s[r_element]-=1
        #             res = s[l:r+1]
        #         else:
        #             return s[l:r+1]
        #     return ""

        def compare_counters(self, counter_s, counter_t):
            for i in counter_t.keys():
                if(i not in counter_s):
                    return False
                if(counter_s[i]<counter_t[i]):
                    return False
            return True


        def minWindow(self, s: str, t: str) -> str:
            counter_t = {}
            for c in t:
                if(c in counter_t):
                    counter_t[c]+=1
                else:
                    counter_t[c]=1
            
            l = 0
            r = 0
            counter_s = {}
            min_len_dict = {}
            while(l<=r and r<len(s)):
                if(s[r] in counter_t):
                    if(s[r] in counter_s):
                        counter_s[s[r]]+=1
                    else:
                        counter_s[s[r]]=1
                r+=1

                while(self.compare_counters(counter_s, counter_t)):
                    leng = r-l+1
                    min_len_dict[leng] = s[l:r]
                    if(s[l] in counter_s):
                        counter_s[s[l]]-=1
                    l+=1

            while(l<r):
                if(s[l] in counter_s):
                        counter_s[s[l]]-=1
                if(self.compare_counters(counter_s, counter_t)):
                        leng = r-l+1
                        min_len_dict[leng] = s[l:r]
                        if(s[l] in counter_s):
                            counter_s[s[l]]-=1
                l+=1
            

            if(len(min_len_dict)==0):
                return ''
            return min_len_dict[min(min_len_dict.keys())]