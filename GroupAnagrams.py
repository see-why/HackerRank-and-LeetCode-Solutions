# https://leetcode.com/problems/group-anagrams/submissions/

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for item in strs:
            item_sorted = "".join(sorted(item))
            if item_sorted not in anagrams:
                anagrams[item_sorted] = []
            anagrams[item_sorted].append(item)
            
        print(anagrams)

        return [list(value) for key, value in anagrams.items()]
