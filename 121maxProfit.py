class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_l = 0
        max_len = 0
        n = len(prices)
        for i in range(n - 1,-1,-1):
            if max_l < prices[i]:
                path_len = 0
                max_l = prices[i]
            else:
                path_len = max_l - prices[i]
            max_len = max(max_len,path_len)
        return max_len


class Solution(object):
    def maxProfit(self, prices):
        min_buy = prices[0]
        res = 0
        for p in prices:
            if p < min_buy:
                min_buy = p
            else:
                res = max(res, p - min_buy)
        return res
