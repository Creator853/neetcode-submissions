
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter after the length
            while s[j] != "#":
                j += 1

            # Extract the length
            length = int(s[i:j])

            # Extract exactly 'length' characters
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move to the beginning of the next length prefix
            i = j + 1 + length

        return result
