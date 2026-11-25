class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647

        # 1. Handle 32-bit overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # 2. Determine sign and work with positive values
        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        quotient = 0
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple

        return -quotient if negative else quotient