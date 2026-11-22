class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        
        while l <= r:
            k = (r + l)//2
            hour = 0
            for p in piles:
                hour += (p+ k - 1) // k
            if hour > h:
                l = k + 1
            else:
                r = k - 1
            
        return l