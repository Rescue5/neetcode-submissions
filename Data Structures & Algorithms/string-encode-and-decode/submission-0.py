class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ""
        dec_key = "#"

        for s in strs:
            encoded_string += s
            dec_key += str(len(s)) + "_"
        
        return encoded_string + dec_key

    def decode(self, s: str) -> List[str]:
        raw_string, key = s.rsplit("#", maxsplit=1)
        print(raw_string, key)
        nums = list(map(int, key.split("_")[:-1]))

        res = []

        for num in nums:
            res.append(raw_string[:num])
            raw_string = raw_string[num:]
        
        return res


