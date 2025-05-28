class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = [0]*26
        for char in magazine:
            a[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if a[ord(char) - ord('a')] > 0:
                a[ord(char) - ord('a')] -= 1
            else:
                return False
        return True

       
        