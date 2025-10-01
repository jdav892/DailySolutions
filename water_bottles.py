class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empty = 0
        while True:
            empty += numBottles
            total += numBottles
            
            newExchanged, leftover = divmod(empty, numExchange)
            if newExchanged == 0:
                break
            
            empty = leftover
            numBottles = newExchanged
        return total 