class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {'(':')','{':'}','[':']'}
        output=[]
        for char in s:
            if char in bracket_dict:
                output.append(char)
            elif output and char == bracket_dict[output[-1]]:
                output.pop()
            else:
                return False
        return not output
            