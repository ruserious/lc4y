import sys

class Solution:
    # @return an integer
    def atoi(self, str):
        flag = 1
        for i,s in enumerate(str):
            if s == ' ':
                continue
            elif s == '+':
                flag = 1
                return self.getAllNumbers(str[i+1:],flag)
                
            elif s == '-':
                flag = -1
                return self.getAllNumbers(str[i+1:],flag)
                
            elif s.isdigit():
                return self.getAllNumbers(str[i:],flag)
                
            else :
                return 0
                


    def getAllNumbers(self, str, flag):
        intb = 0
        defaultRet = 0
        intmax = 2147483647
        intmin = -2147483648
        print "str",str
        if str == "":
            return defaultRet
        for s in str:
            if s.isdigit() == False:
                break
            intb = intb*10 + int(s)

        if flag == 1:
            if intb > intmax:
                return intmax
            else:
                return intb

        if flag == -1:
            if intb*flag < intmin:
                return intmin
            else:
                return intb*flag

s = Solution()
print s.atoi(sys.argv[1])
            
        
