"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are
represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount
 of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        basket = {}
        max_picked = 0
        left = 0
        for right,fruit in enumerate(fruits):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            max_picked = max(max_picked, right - left + 1)
        return max_picked
mysol = Solution()
mysol.totalFruit(fruits = [1,2,1])