''' O(n) time and O(n) memory '''
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

''' O(n) time and O(1) memory '''
def check_permutation_constant_memory(string_one, string_two):
    counts = [0]*128
    result = len(string_one) == len(string_two)

    for character in string_one:
        counts[ord(character)] += 1

    for character in string_two:
        counts[ord(character)] -= 1

    for count in counts:
        result = result and (count == 0)

    return result

if __name__ == '__main__':
    assert check_permutation('caio', 'oiac')
    assert not check_permutation('caio', 'oiab')
    assert not check_permutation('caio', 'oiacm')
    assert check_permutation('banana', 'anaban')
    assert not check_permutation('apple', 'alapp')
    assert check_permutation('','')

    assert check_permutation_constant_memory('caio', 'oiac')
    assert not check_permutation_constant_memory('caio', 'oiab')
    assert not check_permutation_constant_memory('caio', 'oiacm')
    assert check_permutation_constant_memory('banana', 'anaban')
    assert not check_permutation_constant_memory('apple', 'alapp')
    assert check_permutation_constant_memory('','')
