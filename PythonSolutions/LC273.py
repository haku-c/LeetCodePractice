class Solution:
    ones = {
        "0": "",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    teens = {
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
    }
    tens = {
        "0": "",
        "2": "Twenty",
        "3": "Thirty",
        "4": "Forty",
        "5": "Fifty",
        "6": "Sixty",
        "7": "Seventy",
        "8": "Eighty",
        "9": "Ninety",
    }

    def spacers(self, s):
        l = len(s)
        if l >= 10:
            return ["Billion", "Million", "Thousand", ""]
        elif l >= 7:
            return ["Million", "Thousand", ""]
        elif l >= 4:
            return ["Thousand", ""]
        else:
            return [""]

    def translateThree(self, s):
        # logic for getting the hundred and tens...
        l = len(s)
        res = ""
        if l == 0:
            return ""
        if s[0] == "0":
            return self.translateThree(s[1:])
        if l == 3:
            if self.translateThree(s[1:]) != "":
                return self.ones[s[0]] + " Hundred " + self.translateThree(s[1:])
            else:
                return self.ones[s[0]] + " Hundred"
        elif l == 2:
            if s[0] == "1":
                return self.teens[s]
            else:
                if s[1] == "0":
                    return self.tens[s[0]]
                else:
                    if self.ones[s[1]] != "":
                        return self.tens[s[0]] + " " + self.ones[s[1]]
                    else:
                        return self.tens[s[0]]
        else:
            return self.ones[s]
        res = res.strip()
        return res

    def numberToWords(self, num: int) -> str:
        s = str(num)
        intermediate = self.spacers(s)
        if num == 0:
            return "Zero"
        res = ""
        start = 0
        end = len(s) % 3 if (len(s) % 3 != 0) else 3
        for i in range(len(intermediate)):
            w = intermediate[i]
            current = self.translateThree(s[start:end])
            res = " ".join([res, current, w]) if current != "" else " ".join([res])
            start = end
            end = end + 3
        return res.strip()
