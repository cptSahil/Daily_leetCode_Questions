class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
#         basket = {}
#         max_picked = 0
#         left = 0
        
#         for right in range(len(fruits)):
#             basket[fruits[right]] = basket.get(fruits[right],0) + 1
            
#             while len(basket) > 2:
#                 basket[fruits[left]] -= 1
#                 if basket[fruits[left]] == 0:
#                     del basket[fruits[left]]
#                 left += 1
                
#             max_picked = max(max_picked, right-left+1)
            
#         return max_picked

        n=len(fruits)
        i=j=m=0
        x,y=fruits[0],-1
        while j<n:
            if fruits[j]!=x and y==-1:
                y=fruits[j]
            elif fruits[j]!=x and fruits[j]!=y:
                x,y=fruits[j-1],fruits[j]
                m=max(m,j-i)
                i=j-1
                while fruits[i-1]==x:
                    i-=1
            j+=1
        m=max(m,j-i)
        return m
        
        