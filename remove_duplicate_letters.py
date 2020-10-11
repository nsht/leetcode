"""
Remove Duplicate Letters

https://leetcode.com/problems/remove-duplicate-letters/
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

"""
from typing import Dict, List, Tuple


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for index, ch in enumerate(s):
            last_index[ch] = index 
        cur_result = []
        for i, ch in enumerate(s):
            if ch not in cur_result:
                while cur_result and ch < cur_result[-1] and i < last_index[cur_result[-1]]:
                    cur_result.pop()
                cur_result.append(ch)
        return ''.join(cur_result)
                
        
assert Solution().removeDuplicateLetters("bcabc") == "abc"
assert Solution().removeDuplicateLetters("cbacdcbc") == "acdb"
