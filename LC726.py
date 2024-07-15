from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # merge the results
        def recurse(formula):
            track = {}
            element = ""
            number = ""
            i = 0
            while i < len(formula):
                current = formula[i]
                # if you find an uppercase letter, you should add to the dictionary -> iterate until no more lowercase letters
                # to find element name, iterate after to find the numbers
                if current.isupper():
                    ind = i + 1
                    while ind < len(formula) and formula[ind].islower():
                        ind += 1
                    element = formula[i:ind]
                    ind2 = ind
                    while ind2 < len(formula) and formula[ind2].isdigit():
                        ind2 += 1
                    number = int(formula[ind:ind2]) if ind2 > ind else 1
                    track.setdefault(element, 0)
                    track[element] += number
                    i = ind2
                # recurse on the substring if open brace. Be careful the indexing or you will infinite loop
                # increment by index plus 1 here because when we recurse, we start at index 0. Then, the index being returned
                # is the last element tracked by the recursion. We want to go to the element after this so add 1.
                elif current == "(":
                    new_track, index = recurse(formula[i + 1 :])
                    track = Counter(track) + Counter(new_track)
                    i += index + 1
                elif current == ")":
                    ind = i + 1
                    while ind < len(formula) and formula[ind].isdigit():
                        ind += 1
                    number = formula[i + 1 : ind]
                    if number != "":
                        track = {k: v * int(number) for k, v in track.items()}
                    return track, ind
            return track, i

        # we can sort dictionary entries and then join them for a faster concat
        track, _ = recurse(formula)
        return "".join(
            key + str(value) if value > 1 else key
            for key, value in sorted(track.items())
        )


# note this solution avoids string concatenations by reading from the string itself
