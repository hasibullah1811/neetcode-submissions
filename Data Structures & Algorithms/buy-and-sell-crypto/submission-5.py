class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        maxProfit = 0

        while r <= len(prices)-1:
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif prices[l] <= prices[r]:

                if maxProfit < (prices[r] - prices[l]):
                    maxProfit = prices[r] - prices[l]

                r += 1
            else:
                return 0
        return maxProfit
            


            
