class LongestCommonPrefix:

    def longestCommon(self, strs: list[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res    

    @staticmethod
    def main():
        strs = ["flower", "flow", "fl"]  # FIXED: use a list, not a set
        
        obj = LongestCommonPrefix()      # create an instance of the class
        print(obj.longestCommon(strs))   # call the method on the instance

# this must be outside the class
if __name__ == "__main__":
    LongestCommonPrefix.main()
