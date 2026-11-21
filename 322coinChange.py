class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [float('inf')] * (amount + 1)#0-amount个位置，需要+1 
        coins.sort()
        n = len(coins)
        res[0] = 0
        if amount < 0:
            return -1
        for i in range(1,amount + 1):
            for j in range(n):
                if coins[j] > i:
                    break
                res[i] = min(res[i],res[i -  coins[j]] + 1)
        #这里去选择res == -1，如果在for里面，那么-1肯定是算的
        return res [amount] if res[amount] != float('inf') else -1
    
            