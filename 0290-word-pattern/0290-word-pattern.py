class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        map = {}
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in map:
                if map[char] != word:
                    return False
            else:
                map[char] = word
        
        if len(map) != len(set(words)):
            return False
        return True