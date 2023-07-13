class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_dic = {}
            t_dic = {}
            for i in range(len(s)):
                if s[i] not in s_dic:
                    s_dic[s[i]] = 0
                s_dic[s[i]] += 1
                if t[i] not in t_dic:
                    t_dic[t[i]] = 0
                t_dic[t[i]] += 1
            return s_dic == t_dic
        return False