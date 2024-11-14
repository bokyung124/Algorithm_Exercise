class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ''
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_number))
                current_string = ''
                current_number = 0
            elif char == ']':
                prev_string, num = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char

        return current_string

"""
string 합칠 때 `+` 보다 배열에 넣어서 join하는게 더 빠름!
"""