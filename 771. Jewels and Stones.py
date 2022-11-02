"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you
have. Each character in stones is a type of stone you have. You want to know how many of the stones
you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""
jewels = "aA"
stones = "aAAbbbb"


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = {}
        counter = 1
        for word in list(jewels):
            print(word)
            if word in list(stones):
                res.update({word: stones.count(word)})
                counter += 1
        print(res,sum(res.values()))


my_sol = Solution()
my_sol.numJewelsInStones(jewels, stones)
