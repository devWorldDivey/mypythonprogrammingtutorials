"""Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for
the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and
going backward) for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be
[1,1,1,2,1,4,6]. Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.


Example 1:

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

"""


class StockSpanner:

    def __init__(self):
        self.stackOfPrice = []

    def next(self, price: int) -> int:
        res = 1
        self.stackOfPrice.append(price)
        print(self.stackOfPrice)
        for i in range(len(self.stackOfPrice)-1,0,-1):
            print(i)
            if len(self.stackOfPrice) == 1:
                return res
            if self.stackOfPrice[i] < self.stackOfPrice[i - 1]:
                res += 1

        return res


mysol = StockSpanner()
print(mysol.next(100))
print(mysol.next(80))
print(mysol.next(60))