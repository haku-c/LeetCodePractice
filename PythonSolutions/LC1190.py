def reverseParentheses(self, s: str) -> str:
    # since you can reverse a string using slicing, we reverse the relevant substring and concatenate the ends
    def reverse(s, start, end):
        return s[0:start] + s[start : end + 1][::-1] + s[end + 1 : :]

    # basic list queue to track matching parens
    delim = []
    for i in range(len(s)):
        if s[i] == "(":
            delim.append(i)
        elif s[i] == ")":
            s = reverse(s, delim.pop(), i)
    # remove the delimiters before returning
    res = s.replace("(", "")
    res = res.replace(")", "")
    return res
