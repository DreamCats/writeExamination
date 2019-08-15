# __author__: Mai feng
# __file_name__: Palindrome.py
# __time__: 2019:04:08:10:30
def isPalindrome(x: int) -> bool:
    result = True
    a_list = list(str(x))
    print(a_list)
    b_list = list(reversed(a_list))
    print(b_list)
    for i, c in enumerate (a_list):
        if c != b_list[i]:
            result = False
            break
    return result


if __name__ == "__main__":
    result = isPalindrome(x=2008998002)
    print(result)