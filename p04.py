import itertools as it

input = 2


def p04(input):
    output = []
    dict1 = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    str_input = (str)(input)
    a = []
    for i in str_input:
        a.append(dict1[i])

    for e in it.product(*a):
        output.append(''.join(e))

    return output

print(p04(input))
