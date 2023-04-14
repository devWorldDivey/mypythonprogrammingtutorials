# 1. https://leetcode.com/problems/two-sum/ 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solved in O(n) using Dictionary in python
        sol_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in sol_dict:
                sol_dict[nums[i]] = i
            else:
                return [sol_dict[diff],i]


#2. https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    def twoSum1(self, numbers: list[int], target: int) -> list[int]:
        i = 0 
        j = len(numbers)-1
        while i <= j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1   
            else:             
                j -= 1

#3. https://leetcode.com/problems/merge-sorted-array/
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # """
    # Do not return anything, modify nums1 in-place instead.
    # """"
    #Solution using 2 pointers
        #last index nums1
        last = m+n-1
        #merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last -=1
        while n > 0:
            nums1[last] = nums2[n-1]
            n,last=n-1,last-1
            
#4. https://leetcode.com/problems/pascals-triangle/
    def generate(self, numRows: int) -> list[list[int]]:
        res=[[1]]
        
        for i in range(numRows - 1):
            temp =[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        
        return res
    
#5. https://leetcode.com/problems/pascals-triangle-ii/
    def getRow(self, rowIndex: int) -> list[int]:
        res=[[1]]      
        for i in range(rowIndex):
            temp =[0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        print(res[rowIndex])
        return res
    
#6. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        maxprofit = 0
        sell = 0
        for i in prices:
            if i < buy:
                buy = i
            else:
                sell = i
                maxprofit = max(maxprofit,sell-buy)
        print(maxprofit)
        
#7. https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    def maxProfit2(self, prices: list[int]) -> int:
        profit = 0
        buy=prices[0]
        sell=0
        share = 1
        for i in prices:
            if i < buy:
                buy = i
            else:
                sell = i
                if (sell - buy > 0) and share == 1:
                    profit += sell-buy
                    share -= 1
        print(profit)
        

                


        




# Object and method calling
mysol = Solution()
# mysol.twoSum([2,7,11,15], target = 9)
# mysol.twoSum1([2,7,11,15], target = 9)
# mysol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# mysol.generate(numRows = 5 )
# mysol.getRow(rowIndex=0)
# mysol.maxProfit(prices = [7,1,5,3,6,4])
mysol.maxProfit2(prices = [7,1,5,3,6,4])

