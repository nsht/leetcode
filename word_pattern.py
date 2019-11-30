"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


"""

class Solution:
    def wordPattern(self, pattern, string):
        store = {}
        done_list = []
        str_list = string.split()
        if len(str_list) != len(pattern) or string == "":
            return False
        for word_pair in zip(pattern,string.split()):
            if word_pair[0] in store:
                if store[word_pair[0]] != word_pair[1]:
                    return False
            else:
                if word_pair[1] in store.values():
                    return False
                store[word_pair[0]] = word_pair[1]
        return True




# Failed for this input "abc" b c a"

# class Solution:
#     def wordPattern(self, pattern, string):
#         store = []
#         str_list = string.split()
#         if len(str_list) != len(pattern) or string == "":
#             return False
#         for index,word in enumerate(str_list):
#             if word not in pattern:
#                 # print(word)
#                 # print(pattern[index])
#                 if pattern[index] not in store:
#                     str_list = [pattern[index] if q==word else q for q in str_list]
#                     # print(str_list)
#                     store.append(pattern[index])
#         if ''.join(str_list) != pattern:
#             return False
#         else:
#             return True

print(Solution().wordPattern("abba","dog cat cat dog"))
print(Solution().wordPattern("abba","dog cat cat fish"))
print(Solution().wordPattern("aaaa","dog cat cat dog"))
print(Solution().wordPattern("abba","dog dog dog dog"))
print(Solution().wordPattern("abc","b c a"))
