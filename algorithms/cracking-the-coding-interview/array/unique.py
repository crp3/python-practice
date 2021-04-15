'''this has O(n) memory complexity and O(n) time complexity'''
def unique(elements):
    return len(elements) == len(set(elements))

'''version with O(1) memory complexity'''
def unique_constant_memory(elements):
    chars = [0]*128
    for element in elements:
        chars[ord(element)] += 1
    
    for char in chars:
        if char > 1:
            return False

    return True


if __name__ == '__main__':
    assert unique('abcdef')
    assert not unique('aabcdef')
    assert unique('axz')
    assert not unique('abbcd')
    
    assert unique_constant_memory('abcdef')
    assert not unique_constant_memory('aabcdef')
    assert unique_constant_memory('axz')
    assert not unique_constant_memory('abbcd')
 