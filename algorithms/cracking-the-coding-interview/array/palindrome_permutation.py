'''O(n) memory and O(n) time'''
def is_palindrome_permutation(string):
    max_values = 1
    counter_dict = dict()

    for character in string:
        if counter_dict.get(character):
            counter_dict[character] += 1
        else:
            counter_dict[character] = 1

    for key in counter_dict.keys():
        if counter_dict[key] % 2 == 1:
            max_values -= 1
    
    return max_values >= 0

'''O(1) memory and O(n) time'''
def is_palindrome_permutation_constant_memory(string):
    max_values = 1
    counts = [0]*128

    for char in string:
        counts[ord(char)] += 1
    
    for count in counts:
        if count % 2 == 1:
            max_values -= 1
    
    return max_values >= 0

if __name__ == '__main__':
    assert not is_palindrome_permutation('abacab')
    assert is_palindrome_permutation('ababa')
    assert not is_palindrome_permutation('lalllllnllllal')
    assert not is_palindrome_permutation('ccaaaccc')
    assert is_palindrome_permutation('lloooop')
    assert is_palindrome_permutation('acca')
    assert is_palindrome_permutation('aacc')
    assert is_palindrome_permutation('')

    assert not is_palindrome_permutation_constant_memory('abacab')
    assert is_palindrome_permutation_constant_memory('ababa')
    assert not is_palindrome_permutation_constant_memory('lalllllnllllal')
    assert not is_palindrome_permutation_constant_memory('ccaaaccc')
    assert is_palindrome_permutation_constant_memory('lloooop')
    assert is_palindrome_permutation_constant_memory('acca')
    assert is_palindrome_permutation_constant_memory('aacc')
    assert is_palindrome_permutation_constant_memory('')
