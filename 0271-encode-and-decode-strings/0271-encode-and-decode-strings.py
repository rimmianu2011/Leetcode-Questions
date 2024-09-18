class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        global_str = ""
        for s in strs:
            s_len = len(list(s))
            global_str += str(s_len) + "#" + s
        # print(global_str)
        return global_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        str_lst = []
        global_lst = list(s)
        # print(global_lst)

        i = 0
        while i < len(global_lst):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            l = int(s[i:j])
            str_lst.append(s[j+1:j+1+l])
            i = 1 + j + l
        return str_lst
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))