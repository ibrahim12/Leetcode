class Solution:
    # @return an integer
    def atoi(self, my_str):
        n = len(my_str)
        if n == 0:
            return 0

        my_str = my_str.strip()
        my_str = my_str.lower()

        sign = '+'
        if my_str[0] in ['+', '-' ] and my_str[1] in ['+', '-']:
            return 0
        else:
            sign = my_str[0]

        for index in range(n):
            if my_str[index] not in ['+','-','0']:
                my_str = my_str[index:]
                break

        n = len(my_str)

        for index in range(n):
            chr = my_str[index]
            if not ord(chr) >= ord('0') or not ord(chr) <= ord('9'):
                my_str = my_str[:index]
                break

        if my_str == '':
            my_str = 0

        val = int(my_str)

        if sign == '-':
            val = -val

        if val >= 2147483648:
            val = 2147483647

        if val <= -2147483648:
            val = -2147483648


        return val



s = Solution()
# for index in range(1,10):
print( s.atoi("-2147483649") )