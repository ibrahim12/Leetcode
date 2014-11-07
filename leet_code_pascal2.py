class Solution:
    # @return a list of lists of integers

    def _gen(self, n, final):
        if n == 0:
            return []
        if n == 1:
            final.append([1])
            return final

        final = self._gen( n - 1, final)
        # print(n,final)
        prev = final[ n - 2 ]
        # print(n, prev, final)
        result = [1]
        for index in range(1, n-1):
            result.append(prev[index-1]+prev[index])

        result.append(1)
        # print(n, result)

        final.append(result)

        return final

    def getRow(self, rowIndex):
        tr =  self._gen(rowIndex+1, [])
        return tr[rowIndex]



s = Solution()
print( s.getRow(1) )