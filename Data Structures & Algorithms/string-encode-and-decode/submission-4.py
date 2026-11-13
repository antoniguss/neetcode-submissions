class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            nextLen = 0
            while ord(s[i]) - ord('0') <= 9 and s[i] != '#':
                nextLen = nextLen*10 + ord(s[i]) - ord('0')
                i += 1
            result += [s[i+1:i+1+nextLen]]
            i += nextLen
            i += 1
            

        return result

