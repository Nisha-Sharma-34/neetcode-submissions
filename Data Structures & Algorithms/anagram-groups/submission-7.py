class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for word in strs:
            sorted_word=''.join(sorted(word))
            dict[sorted_word].append(word)
        return list(dict.values())


                
                

                
                
            

        