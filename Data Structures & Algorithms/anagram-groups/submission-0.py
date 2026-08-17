class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = defaultdict(list)               #mapping charCount to list of Anagrams
                                                      #changed hashmap to default hashmap where
        for s in strs:                                #default value is a list to not deal with one edge case 
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord('a')] += 1       # a = 0, z = 25; 
                                                    # a = 80 -> 80 - 80
            anagramsDict[tuple(count)].append(s)     # b = 81 -> 81 - 80
                                                    # count is list, list cannot be keys
        return list(anagramsDict.values())                 # changed count list to tuple since 
                                                    # they are non-mutable
                                    # method to return values 
                                    # (anagrams grouped together)
                                    # instead of keys to display results
                                    # Optimal O(m * n) soln:
                                    # m is num of strs
                                    # n is avg. length (num of char) 
                                    # of each str
                                    # returned as list due to TypeError 
                                    # (return type needs to be List[List[str]]) 