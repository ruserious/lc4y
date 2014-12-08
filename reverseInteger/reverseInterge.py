import sys
class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0 :
            return 0
        
        flag = 1
        if x < 0 :
            x = -x
            flag = -1
        current = 0
        while x/10 > 0 :
            current = (x % 10 ) + 10 * current
            x /= 10

        current = current * 10 + (x % 10)

        if flag == 1:
            if current>>31 > 0 :
                current = 0
        else :
            if ((current * flag)>>31) &1 != 1:
                current = 0
            else :
                current = current * flag
                
        return current*flag


s = Solution()
print s.reverse(int(sys.argv[1]))
            
