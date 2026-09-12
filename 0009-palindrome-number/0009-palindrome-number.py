class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        palindrome = 0
        left = 0
        right = len(s) -1

        while(left <= right):
            if s[left]==s[right]:
                palindrome = 1
            
            else:
                palindrome = 0
                break
            left +=1
            right -=1
        
        if palindrome ==1:
            return True
        
        else:
            return False