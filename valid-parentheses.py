class Solution:
    def isValid(self, s: str) -> bool:
        match = {')':'(', '}':'{', ']':'['}
        lst = []
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                lst.append(s[i])
            else:
                if not lst or lst.pop() != match[s[i]]:
                    return False
        if lst:
            return False
        return True