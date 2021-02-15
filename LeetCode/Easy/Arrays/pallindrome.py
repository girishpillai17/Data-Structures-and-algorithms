"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads - 121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
#Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false
"""

class Solution:
    def isPalindrome(self, num: int) -> bool:
        temp = 0
        x = abs(num)

        while x != 0:
            n = x % 10
            temp = (temp*10) + n
            x = x//10
            
        if num >= 0:      #Only check for positive as if the number is negative it wont be pallindrome even if digits are exactly same
            rev_ = temp

        if -2**31 <= num <= 2**31-1 and num >= 0 and num == rev_: #checking if the number is postive, if positive then check if its pallindrome
            return True
        else:
            return False

t = Solution()
t.isPalindrome(-101)
