# __author__: Mai feng
# __file_name__: RomanToInt.py
# __time__: 2019:04:08:12:53



def romanToInt(s: str) -> int:
    res = 0
    a_list = list(s)
    a_dict = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    for i, a in enumerate (a_list):
        b = a_dict[a]
        if i + 1 != len(a_list):
            c = a_dict[a_list[i + 1]]
            if c > b:
                b = -b
        res = res + b
    res = int(res)
    if res < 0 or res >3999:
        return 0
    return res

if __name__ == "__main__":
    res = romanToInt('IV')
    res = romanToInt('III')
    res = romanToInt('IX')
    res = romanToInt('LVIII')
    res = romanToInt('MCMXCIV')
    print(res)