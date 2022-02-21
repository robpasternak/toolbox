from toolbox.everyother import everyother

def test_everyother():
    assert everyother([1,2,3,4,5]) == [2,4]
    assert everyother() == []
