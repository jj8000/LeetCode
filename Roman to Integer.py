s = "MMMCI"


def RomanToInt(s: str) -> int:
    s_list = [num for num in s]
    result = 0
    while len(s_list) > 1:
        if s_list[-1] == 'I':
            result += 1
            del s_list[-1]
        elif s_list[-1] == 'V':
            if s_list[-2] == 'I':
                result += 4
                del s_list[-2:]
            else:
                result += 5
                del s_list[-1]
        elif s_list[-1] == 'X':
            if s_list[-2] == 'I':
                result += 9
                del s_list[-2:]
            else:
                result += 10
                del s_list[-1]
        elif s_list[-1] == 'L':
            if s_list[-2] == 'X':
                result += 40
                del s_list[-2:]
            else:
                result += 50
                del s_list[-1]
        elif s_list[-1] == 'C':
            if s_list[-2] == 'X':
                result += 90
                del s_list[-2:]
            else:
                result += 100
                del s_list[-1]
        elif s_list[-1] == 'D':
            if s_list[-2] == 'C':
                result += 400
                del s_list[-2:]
            else:
                result += 500
                del s_list[-1]
        elif s_list[-1] == 'M':
            if s_list[-2] == 'C':
                result += 900
                del s_list[-2:]
            else:
                result += 1000
                del s_list[-1]
    num_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    if len(s_list) == 1:
        result += num_dict[s_list[0]]
    return result


print(RomanToInt("CMXLIX"))
