"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

 

Note:

    1 <= words.length <= 50
    1 <= pattern.length = words[i].length <= 20

"""

class Solution:
    def findAndReplacePattern(self, words, pattern):
        solution = []
        if not words or not pattern:
            return []
        for word in words:
            result = self.wordPattern(pattern,word)
            if result:
                solution.append(word)
        return solution

    def wordPattern(self, pattern, string):
        store = {}
        done_list = []
        for word_pair in zip(pattern,string):
            if word_pair[0] in store:
                if store[word_pair[0]] != word_pair[1]:
                    return False
            else:
                if word_pair[1] in store.values():
                    return False
                store[word_pair[0]] = word_pair[1]
        return True


print(Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))
