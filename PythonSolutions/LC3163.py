class Solution:
    def compressedString(self, word: str) -> str:
        temp = []
        past = word[0]
        segment = 1
        for i in range(1, len(word)):
            if segment == 9:
                temp.append(str(segment))
                temp.append(past)
                past = word[i]
                segment = 0
            if past == word[i]:
                segment += 1
            else:
                temp.append(str(segment))
                temp.append(past)
                past = word[i]
                segment = 1
        temp.append(str(segment))
        temp.append(past)
        comp = "".join(temp)
        return comp


# again the concatenation of the array at the end is faster then concatenating in the loop
