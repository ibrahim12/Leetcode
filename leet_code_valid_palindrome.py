class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):

        # import re
        # s = re.sub(r'[^a-zA-z]+','', s)
        s = s.lower()

        str = []
        for index in s:
            value = ord(index)
            if ( value >= ord('a') and value <= ord('z')) or ( value >= ord('0') and value <= ord('9')):
                str.append(index)

        s = ''.join(str)

        n = len(s)

        end = n - 1
        for index in range(n):
            if s[index] != s[end - index]:
                return False

        return True



str = '0k.;r0.k;'
s = Solution()
str1 = s.isPalindrome(str)

print(str1)