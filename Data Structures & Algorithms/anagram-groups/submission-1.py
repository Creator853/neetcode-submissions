class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen: dict[str, List[str]] ={}
        for s in strs:
            key=''.join(sorted(s))
            if key not in seen:
                seen[key] = [s]
            else:
                seen[key].append(s)
        return list(seen.values())
