class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        r={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        result=[""]
        for i in digits:
            l=r[i]
            result=[combo + letter for combo in result for letter in l]
        return result