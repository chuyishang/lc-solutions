class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        best, low, high = prices[1] - prices[0], prices[0], prices[1]
        for i in range(len(prices)-1):
            if prices[i] < low:
                low = prices[i]
                high = prices[i+1]
            if prices[i+1] > high:
                high = prices[i+1]
            if high - low > best:
                best = high - low
        if best > 0:
            return best
        else:
            return 0