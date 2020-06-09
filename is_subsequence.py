class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slist = list(s)
        for x in t:
            if len(slist) == 0:
                return True
            if x == slist[0]:
                slist.pop(0)
        if len(slist) == 0:
            return True
        return False



print(Solution().isSubsequence("abc","ahbgdc")==True)
