

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):

        n = len(matrix)
        level_count = n//2


        for level in range(level_count):
            # print('-')
            # level = 0
            end = n - 1 - 2 * level
            for pos in range(end):
                # print(level, pos)
                # print(level,level+pos, '-', n - 1 - pos - level, level)
                # print(n - 1 - pos - level,level, '-', n - 1 - level, n - 1 - pos - level )
                # print(n - 1 - level,n - 1 - pos - level , '-', level + pos, n - 1 - level )

        # pos = 1
                matrix[level][level+pos], matrix[n - 1 - pos - level][level] =  matrix[n - 1 - pos - level][level] , matrix[level][level+pos]
                matrix[n - 1 - pos - level][level] , matrix[n - 1 - level][ n - 1 - pos - level ] = matrix[n - 1 - level][ n - 1 - pos - level ] , matrix[n - 1 - pos - level][level]
                matrix[n - 1 - level][ n - 1 - pos - level ] , matrix[ level + pos ][ n - 1 - level  ] = matrix[ level + pos ][ n - 1 - level ], matrix[n - 1 - level][ n - 1 - pos - level ]

        return matrix

def printM(m):
    for a in m:
        print(a)

matrix = [ ['a','b','c','d'], ['e','f','g','h'], ['i','j','k','l'], ['m','n','o','p']]
matrix2 = [[1,2],[3,4]]

s = Solution()

printM(matrix)
s.rotate(matrix)
print('')
printM(matrix)

