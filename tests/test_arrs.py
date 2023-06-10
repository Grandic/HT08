from utils import arrs, dicts
from utils.dicts import data

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([1, 2, 3, 4, 5], 3, "test") == 4
    assert arrs.get([1, 2, 3, 4, 5], 4, "test") == 5
    assert arrs.get([], -1, "test") == "test"

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([2], 0) == [2]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1], -2) == [1]

def test_dicts():
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data, "vvv", "test") == "test"
    assert dicts.get_val(data, "bomg") == "shoot"
    assert dicts.get_val(data, "petka") == "vasilii_ivanovi4"
    assert dicts.get_val(data, "doroga") == "v_nebo"
    assert dicts.get_val({}, "doroga") == "git"
    assert dicts.get_val({}, "doroga", "test") == "test"