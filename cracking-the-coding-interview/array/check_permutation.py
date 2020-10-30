def check_permutation(string_one, string_two):
    counter_dict = dict()
    result = len(string_one) == len(string_two)

    for character in string_one:
        if counter_dict.get(character):
            counter_dict[character] += 1
        else:
            counter_dict[character] = 1
    
    for character in string_two:
        if counter_dict.get(character):
            counter_dict[character] -= 1
        
    for key in counter_dict.keys():
        result = result and (counter_dict[key] == 0)

    return result

if __name__ == '__main__':
    assert check_permutation('caio', 'oiac')
    assert not check_permutation('caio', 'oiab')
    assert not check_permutation('caio', 'oiacm')
    assert check_permutation('banana', 'anaban')
    assert not check_permutation('apple', 'alapp')
    assert check_permutation('','')