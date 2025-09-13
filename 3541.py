class Solution:
    def maxFreqSum(self, s):
        vowel = [s.count(x) for x in s if x in 'aeiou']
        consonant = [s.count(x) for x in s if x not in 'aeiou']
        if vowel and consonant:
            return max(vowel) + max(consonant)
        if (not vowel) and consonant:
            return max(consonant)
        return max(vowel)


sol = Solution()
print(sol.maxFreqSum("aeiaeia"))
