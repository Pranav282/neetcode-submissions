class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=[]
        for i in range(len(prices)):
            max_profit=0
            j=i+1
            while j>i and j<len(prices):
                current_profit = prices[j] - prices[i]
                max_profit=max(max_profit,current_profit)
                j+=1
            res.append(max_profit)
        return max(res)                   