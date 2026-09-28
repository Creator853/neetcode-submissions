class Solution:
    def groupAnagrams(self, 
                      strs: List[str]
                    ) -> List[List[str]]:
        seen : dict[str, List[int]] = {}
        output: List[List[str]] = []
        for i,s in enumerate(strs):
            s = ''.join(sorted(s))
            
            if s not in seen:
                seen[s]=[i]
            else:
                seen[s].append(i)
        for positions in seen.values():
            group = []
            for i in positions:
                group.append(strs[i])
            output.append(group)
        return output