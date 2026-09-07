class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        elif word.isupper():
            return True
        elif word == word.capitalize():
            return True
        return False
