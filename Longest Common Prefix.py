

def longestCommonPrefix(strs: list[str]) -> str:
    temp = set()
    prefix = ""
    flag = True
    count = 0
    while flag is True and prefix not in strs:
        for string in strs:
            temp.update(string[count])
        if len(temp) == 1:
            prefix += temp.pop()
            count += 1
        else:
            flag = False
    return prefix


l = ['', 'casa', 'car']
longestCommonPrefix(l)




