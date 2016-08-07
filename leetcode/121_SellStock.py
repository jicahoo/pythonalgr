class Solution(object):
    def maxProfit_use_heap(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        h=[]
        import heapq
        heapq.heappush(h, prices[0])
        n = len(prices)
        max_delta = 0
        for i in xrange(1, n):
            min_before_i = h[0]
            cur = prices[i]
            delta = cur - min_before_i
            if delta > max_delta:
                max_delta = delta
            heapq.heappush(h, cur)
        return max_delta

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        max_delta = 0
        # No need to use heap. Firstly, I tried to use heap to keep the min value. Actually, heap is unnecessary.
        min_buy_in = prices[0]
        for i in xrange(1, n):
            cur = prices[i]
            delta = cur - min_buy_in
            if delta > max_delta:
                max_delta = delta
            if cur < min_buy_in:
                min_buy_in = cur
        return max_delta

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([7,6,4,3,1])
    print s.maxProfit([7])
    print s.maxProfit([])