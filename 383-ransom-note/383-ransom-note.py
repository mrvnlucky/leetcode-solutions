class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # check ransomNote characters 1 by 1
        for i in range(len(ransomNote)):
            char = ransomNote[i]
            # look for matching character in magazine string
            matchIndex = magazine.find(char)
            if matchIndex == -1:
                return False
            
            magazine = magazine[:matchIndex] + magazine[matchIndex+1:]
        return True