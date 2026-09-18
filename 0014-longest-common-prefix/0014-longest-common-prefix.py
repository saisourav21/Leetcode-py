class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        for i in range (len(strs[0])):
            try:
                for string in strs[1:]:
                    if string[i] != strs[0][i]:
                        return prefix
                prefix +=strs[0][i]

            except IndexError:
                return prefix   

        return prefix