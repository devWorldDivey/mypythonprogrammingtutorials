"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
"""
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        result = 0
        for boxes in sorted(boxTypes, reverse=True, key=lambda x: x[1]):
            if truckSize > 0:
                if boxes[0] < truckSize:
                    result += (boxes[1] * boxes[0])
                else:
                    result += (boxes[1] * truckSize)
                truckSize -= boxes[0]
        return result


mysol = Solution()
mysol.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)