import sys
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1 :
            return s
        direction = 1
        result = [""] * nRows
        count = 0
        for i in s:
            if direction == 1 and count < nRows-1:
                result[count] += i
                count += 1
            elif direction == 1 and count == nRows-1:
                result[count] += i
                direction = -1
                count -= 1
            elif direction == -1 and count > 0:
                result[count] += i
                count -= 1
            elif direction == -1 and count == 0:
                result[count] += i
                direction = 1
                count += 1
            else :
                pass

        ret = "".join(result)
        return ret

s=Solution()
ret=s.convert(sys.argv[1],2)
print ret
#if ret == sys.argv[2]:
#    print "bingo"
