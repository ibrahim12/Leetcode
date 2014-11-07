class Solution:
    # @return a string

    def _count(self, n ):
        if n == 0:
            return []
        if n == 1:
            return ['1']

        prev = self._count(n - 1)
        n = len(prev)

        if not n:
            return []

        result = []
        count = 1
        current = prev[0]
        for index in range(1,n):
            if current != prev[index]:
                result.append(str(count))
                result.append(current)
                current = prev[index]
                count = 1
            else:
                count += 1

        result.append(str(count))
        result.append(current)
        return result

    def countAndSay(self, n):
        result =  self._count(n)
        return ''.join(result)




s = Solution()
# for index in range(1,10):
print( s.countAndSay(30) )