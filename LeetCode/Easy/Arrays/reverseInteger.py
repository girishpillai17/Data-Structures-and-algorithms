"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverseInteger(self, num: int) -> int:
        flag = -1
        temp = 0
        x = abs(num)

        for i in range(len(str(abs(num)))):
            n = x % 10
            temp = (temp*10) + n
            x = x//10
        if num > 0:
            rev_ = temp
        else:
            rev_ = temp * flag

        if -2**31 <= rev_ <= 2**31-1:
            return rev_
        else:
            return 0

