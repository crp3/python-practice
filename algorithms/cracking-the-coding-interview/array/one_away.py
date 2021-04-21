def one_away(str1, str2):
    if len(str1) == len(str2):
        return one_replace(str1, str2)
    elif len(str1) == len(str2)+1:
        return one_insert(str1, str2)
    elif len(str2) == len(str1)+1:
        return one_insert(str2, str1)
    else:
        return False

def one_replace(str1, str2):
    edited = False
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            if edited:
                return False
            edited = True
        i += 1
    return True

def one_insert(str1, str2):
    i = len(str1)-1
    j = len(str2)-1
    edited = False
    while i >= 0 and j >= 0:
        if str1[i] != str2[j]:
            if edited:
                return False
            edited = True
            i -= 1
        else:
            i -= 1
            j -= 1
    return True

if __name__ == '__main__':
    assert one_away("pale", "pale") == True
    assert one_away("", "") == True
    # one insert
    assert one_away("pale", "ple") == True
    assert one_away("ple", "pale") == True
    assert one_away("pales", "pale") ==  True
    assert one_away("ples", "pales") == True
    assert one_away("pale", "pkle") == True
    assert one_away("paleabc", "pleabc") == True
    assert one_away("", "d") == True
    assert one_away("d", "de") == True
    # one replace
    assert one_away("pale", "bale") == True
    assert one_away("a", "b") == True
    assert one_away("pale", "ble") == False
    # multiple replace
    assert one_away("pale", "bake") == False
    # insert and replace
    assert one_away("pale", "pse") == False
    assert one_away("pale", "pas") == False
    assert one_away("pas", "pale") == False
    assert one_away("pkle", "pable") == False
    assert one_away("pal", "palks") == False
    assert one_away("palks", "pal") == False
    # permutation with insert shouldn't match
    assert one_away("ale", "elas") == False