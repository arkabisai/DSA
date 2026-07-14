class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Dictionary storing Roman numeral values in descending order.
        # Special cases like 900 (CM), 400 (CD), etc. are included.
        dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        # Stores the final Roman numeral
        result = ""

        # Traverse the dictionary from largest value to smallest
        for i in dict:
            # Keep using the current Roman numeral while num is large enough
            while num >= i:
                # Append the corresponding Roman symbol
                result += dict[i]

                # Reduce the number by the current value
                num -= i

        # Return the final Roman numeral string
        return result