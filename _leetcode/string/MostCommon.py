""" Question - Decoded string
    Given an encoded string, return its decoded string.
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    METHOD :
        - If element is nt a closing bracket, add it to the stack
        - else if element is a closing bracket, pop the substrings out,
        followed by the digit, and then multiply digit by string add the result back the stack and repeat the process
"""


def decodeString(s: str) -> str:

    stack = []
    for idx in range(len(s)):
        if s[idx] != "]":
            stack.append(s[idx])
        else:
            substr = ""
            # Keep popping until you encounter an closing bracket "["
            while stack[-1] != "[":
                substr = stack.pop() + substr
            # throw-away the opening bracket bracket at the top now
            stack.pop()
            # Now get the number
            numbr = ""
            while stack and stack[-1].isnumeric():
                numbr = stack.pop() + numbr
            # Multiply the number with the substring and add back to the stack
            stack.append(int(numbr) * substr)

    return "".join(stack)

