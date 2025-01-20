class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        rep1 = list(bin(num1))[2:]
        set2 = bin(num2).count("1")
        set1 = bin(num1).count("1")

        if set1 == set2:
            return num1
        elif set2 < set1:
            # left to right of rep1 and unset set bits
            i = 0
            while i < len(rep1):
                if rep1[i] == "1" and set2 > 0:
                    set2 -= 1
                else:
                    rep1[i] = "0"
                i += 1
        elif set2 > set1:
            # right to left set unset bits to 1
            for i in range(len(rep1) - 1, -1, -1):
                if rep1[i] == "0":
                    rep1[i] = "1"
                    set1 += 1
                if set2 == set1:
                    break
            while set2 > set1:
                rep1.append("1")
                set1 += 1
        return int("".join(rep1), 2)


# a bit more elegant solution for the case where set2 > set1 can occur if you look at the bounds and just fill from an array of size 31
# instead of appending


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31  # Start from the most significant bit.

        # While result has fewer set bits than num2
        while set_bits_count < target_set_bits_count:
            # If the current bit of num1 is set or we must set all remaining bits in result
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1  # Move to the next bit.

        return result

    # Helper function to check if the given bit position in x is set (1).
    # (1 << bit) --> shifts a 1 left bit number of times
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in x to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)


# a good idea here is to think about how checking for each set in the number can be done without complete conversion to binary
