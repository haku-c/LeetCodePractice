class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        delim = ">"
        res = []
        for s in strs:
            res.append(str(len(s)) + delim + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        n = len(s)
        res = []
        start = 0
        i = 1
        while i < n:
            if s[i] == ">":
                number = int(s[start:i])
                res.append(s[i + 1 : i + 1 + number])
                start = i + 1 + number
                i = start + 1
            else:
                i += 1
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# use a delimiter, but also use the frame idea where you specify the number of characters in the next string
# this allows you to use any character as a delimiter without the need to escape
