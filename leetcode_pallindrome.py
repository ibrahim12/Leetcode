class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        div = 1
        while x // div >= 10:
            div *= 10

        while x:
            r = x % 10
            l = int(x // div)


            if l != r:
                return False

            x = int(( x % div ) // 10)
            div /= 100

        return True


s = Solution()
print( s.isPalindrome(112211))
