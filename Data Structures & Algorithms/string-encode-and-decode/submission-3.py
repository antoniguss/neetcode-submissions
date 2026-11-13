class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += s.replace(",", "\\,") + " , "
        return result

    def decode(self, s: str) -> List[str]:
        return [separated.replace("\\,", ",") for separated in s.split(" , ")][:-1]

