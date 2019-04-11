def isValid(s: str) -> bool:
    if s == "":
        return True
    stack = []
    symbols = {'(':')','{':'}','[':']'}
    keys = list(symbols.keys())
    for one in s:
        if one in keys:
            stack.append(one)
        else:
            if stack == []:
                return False
            top = stack.pop()
            if symbols[top] != one:
                return False
    if stack != []:
        return False
    return True




if __name__ == "__main__":
    import time
    start = time.time()
    s = "()"
    # s = '{[]}'
    s  = "()[]{}"
    # s = "(]"
    # s = "([)]"
    # s = "]"
    # s = "){"
    # s = "(("
    # s = "))"
    res = isValid(s)
    print(res)
    end = time.time()
    print('时间:', (end-start))
