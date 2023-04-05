"""
You are given two 2D integer arrays, items1 and items2, representing two sets of items.
 Each array items has the following properties:
items[i] = [valuei, weighti] where valuei represents the value and weighti
represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the
 sum of weights of all items with value valuei.
Note: ret should be returned in ascending order by value.
Example 1:
Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
Output: [[1,6],[3,9],[4,5]]
"""
class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        dict1 = {}
        for i in range(len(items1)):
            dict1.update({items1[i][0]:items1[i][1]})
        for j in range(len(items2)):
            if items2[j][0] not in dict1:
                dict1.update({items2[j][0]:items2[j][1]})
            else:
                dict1.update({items2[j][0]:dict1[items2[j][0]]+items2[j][1]})
        res = []
        for k in sorted(dict1):
            res.append([k,dict1[k]])
        print(res)
mysol = Solution()
mysol.mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]])