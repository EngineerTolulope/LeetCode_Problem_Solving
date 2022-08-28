class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        infinity = float('infinity')
        prices = [infinity] * n
        prices[src] = 0
        
        for _ in range(k + 1):
            temp_prices = prices.copy()
            
            for source, destination, price in flights:
                # if prices[source] == infinity:
                #     continue
                if prices[source] + price < temp_prices[destination]:
                    temp_prices[destination] = prices[source] + price              
            prices = temp_prices
        return prices[dst] if prices[dst] != infinity else -1