class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        res=[]
        for i in range(len(prices)-1):
            if max( prices[i+1:] ) - prices[i] < 0:
                max_profit = 0
            else:
                max_profit=max( prices[i+1:] ) - prices[i]
            res.append(max_profit)
        return max(res)