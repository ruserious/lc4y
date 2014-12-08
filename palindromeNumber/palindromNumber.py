import sys

class Solution:
    def isPalindrome(self, x):
        origin = x
        reverse = 0

        if x < 0:
            return False
        
        while x != 0 :
            reverse = reverse*10 + (x%10)
            x /= 10

        if origin == reverse:
            return True

        return False

s = Solution()
print s.isPalindrome(int(sys.argv[1]))
