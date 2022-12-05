"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.



Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

"""
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        dict1 = {}
        for i in range(len(names)):
            dict1.update({heights[i]: names[i]})
        print(dict1)
        output = []
        for j in sorted(dict1,reverse=True):
            output.append(dict1[j])
        print(output)


my_sol = Solution()
my_sol.sortPeople(names, heights)
