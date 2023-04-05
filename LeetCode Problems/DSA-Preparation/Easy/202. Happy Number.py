class Solution:
    def isHappy(self, n: int) -> bool:
        newnum = 0
        res = []
        while (1 not in res):
            for i in str(n):
                newnum += int(i)*int(i)
            if newnum not in res:
                res.append(newnum)
            else:
                break
            n = newnum
            newnum = 0

        print(res)
mysol = Solution()
mysol.isHappy(n=7)



