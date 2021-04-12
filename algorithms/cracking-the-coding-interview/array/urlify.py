def urlify(string, length):
    listed_string = list(string)
    i = len(string)-1
    j = length-1
    while i >= 0:
        if listed_string[j] == ' ':
            listed_string[i] = '0'
            listed_string[i-1] = '2'
            listed_string[i-2] = '%'
            i -= 3
        else:
            listed_string[i] = listed_string[j]
            i -= 1 
        j -= 1
    return to_string(listed_string)

def to_string(arr):
    s = ''
    for character in arr:
        s += character
    return s

if __name__ == '__main__':
    string = 'Mr John Smith    '
    string2 = 'much ado about nothing      '
    assert urlify(string, 13) == 'Mr%20John%20Smith'
    assert urlify(string2, 22) == 'much%20ado%20about%20nothing'
    