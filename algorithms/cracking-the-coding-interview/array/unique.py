def unique(elements):
    return len(elements) == len(set(elements))

if __name__ == '__main__':
    assert unique([1,2,3,4,5])
    assert not unique([1,1,2,3,4,5])
    assert unique([1,10,100])
    assert not unique([1,10,100,100,1000])