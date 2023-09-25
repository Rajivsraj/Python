class Solution(object):
    def maxProfit(self, prices):

        mi = min(prices)
        mi_index = prices.index(mi)

        mx = max(prices[mi_index:])

        mx_index = prices.index(mx)

        if mi_index < mx_index:
            profit = mx - mi
        else:
            profit = 0

        return profit


prices = [2,4,1]
obj = Solution()
print(obj.maxProfit(prices))