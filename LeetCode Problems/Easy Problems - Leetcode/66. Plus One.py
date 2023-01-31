class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                print(digits)
                return digits
        digits.append(0)
        digits[0] = 1
        print(digits)
        return digits

mysol = Solution()
mysol.plusOne(digits = [1,3,9])
