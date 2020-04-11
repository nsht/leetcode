class Solution:
    def backspaceCompare(self, S, T):
        fs, ft, s1, t1 = 0, 0, "", ""
        for x in reversed(S):
            if x == "#":
                fs += 1
                continue
            if fs:
                fs -= 1
                continue
            s1 += x

        for x in reversed(T):
            if x == "#":
                ft += 1
                continue
            if ft:
                ft -= 1
                continue
            t1 += x
        return s1 == t1


S = "ab#c"
T = "ad#c"
print(Solution().backspaceCompare(S, T))
S = "ab##"
T = "c#d#"
print(Solution().backspaceCompare(S, T))
S = "a#c"
T = "b"
print(Solution().backspaceCompare(S, T))

S = "xywrrmp"
T = "xywrrmu#p"

print(Solution().backspaceCompare(S, T))


#method 2 
