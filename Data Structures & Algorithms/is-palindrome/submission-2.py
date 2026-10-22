class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            l_isalnum = s[left].isalnum()
            r_isalnum = s[right].isalnum()
            if l_isalnum and r_isalnum:
                if s[left].lower() != s[right].lower():
                    return False
            elif not l_isalnum and r_isalnum:
                left += 1
                continue
            elif l_isalnum and not r_isalnum:
                right -= 1
                continue
            left += 1
            right -= 1

        return True
