"""
1021. Remove Outermost Parentheses
Easy

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""
import pdb

class Solution:
    def removeOuterParentheses(self, S):
        s_list = [x for x in S]
        counter = 0
        output = ""
        for x in s_list:
            if counter == 0 and x == "(":
                counter += 1
            elif counter == 1 and x == ")":
                counter -= 1
            elif x == "(":
                counter +=1
                output += x
            elif x == ")":
                counter -=1
                output += x
        return output


print(Solution().removeOuterParentheses("(()())(())")) #"()()()"
print(Solution().removeOuterParentheses("(()())(())(()(()))")) #"()()()()(())"
print(Solution().removeOuterParentheses("()()")) #""


# assert Solution().removeOuterParentheses("(()())(())") == "(()())(())","Error"