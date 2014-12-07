import sys
class Solution:
    # return string
    def longestPalindrome(self, s):
        if s == "" or s == None:
            return s
        else :
            maxlen=1
            maxstr=s[0]
        
            higher = len(s)
            center = 1
            # odd
            while center < higher -1 :
                i = 1
                while center - i >= 0 and center + i < higher :
                    if s[center-i] != s[center+i]:
                        break
                    else :
                        if maxlen < (2*i+1):
                            maxlen = 2*i+1
                            maxstr = s[center-i:center+i+1]
                        i = i + 1
                center = center+1
            # even
            begin = 0
            while begin < higher-1:
                left = begin
                right = begin + 1
                while left >=0 and right < higher:
                    if s[right] == s[left]:
                        if maxlen < right - left+1:
                            if right-left >= 1:
                                maxlen = right-left+1
                                maxstr = s[left:right+1]
                                print "maxstr",maxstr
                        left = left - 1
                        right = right + 1
                    else :
                        break
                begin = begin + 1            
            return maxstr        
                
                    
        
    def generateAllSubstring(self, s, result):
        if s == "" or s == None:
            return
        else:
            result.append(s)
            self.generateAllSubstring(s[:len(s)-1], result)
            self.generateAllSubstring(s[1:len(s)], result)

    def generate(self, s):
        result = []
        for i in range(len(s)-1):
            for j in range(1,len(s)):
                result.append(s[i:j])
        return result
    
    def isPalindrome(self, s):
        if s == self.reverse(s):
            return True
        else :
            return False
    def reverse(self, ins):
        return ins[::-1]
    
s=Solution()


#s.generateAllSubstring("abcdzeusnilemacaronimaisanitratetartinasiaminoracamelinsuez" ,ret)
#ret=s.longestPalindrome("zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez")
ret=s.longestPalindrome(sys.argv[1])
print ret



