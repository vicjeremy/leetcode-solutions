# Last updated: 1/29/2026, 5:55:06 PM
class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        bracket = {')':'(','}':'{', ']':'['}
        for char in s:
            if char in bracket:
                if seen and seen[-1] == bracket[char]:
                    seen.pop()  
                else:
                    return False
            else: 
                seen.append(char)
        return not seen
