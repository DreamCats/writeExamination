
def longestCommonPrefix(strs: list) -> str:
    c = ''
    d = 0
    if len(strs) == 0:
        return c
    if len(strs) == 1:
        return strs[0]
    for i, b in enumerate (strs[0]):
        for j in range(1, len(strs)):
            if len(strs[j]) == 0:
                return ''
            if i == len(strs[j]):
                d = 1
                break
            if b == strs[j][i]:
                if j == len(strs) - 1:
                    c += b
            else:
                d = 1
                break
        if d == 1:
            break
    return c


if __name__ == "__main__":
    res = longestCommonPrefix(["flower","flow","flight"])
    res = longestCommonPrefix(["c","acc","ccc"])
    # res = longestCommonPrefix([])
    res = longestCommonPrefix(["abab","aba",""])
    # res = longestCommonPrefix(["abab","",""])
    # res = longestCommonPrefix(["","",""])
    # res = longestCommonPrefix(["ab"])
    # res = longestCommonPrefix(["ab", 'a', 'a'])
    print(res)

