'''
Not executed on leetcode.
Time - O(N^2)
Space - O(1)
Approach:
Assumption - word1 and word2 can never be equal.
1. 2 pointer approach, first pointer contains the location of word1 and 2nd pointer contains the location of word2.
2. Iterate over the words list and calculate minimum distance among 2 words by using pointer locations.
'''
class Solution:
    def shortestDistance(self, words, word1, word2):
        i1 = -1
        i2 = -1

        minDistance = float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            if words[i] == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i1-i2))

        return minDistance

sol = Solution()
words = ["practice","makes","perfect","coding","makes"]
print(sol.shortestDistance(words,"coding","makes"))