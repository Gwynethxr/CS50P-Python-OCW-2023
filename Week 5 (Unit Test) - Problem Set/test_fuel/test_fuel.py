from fuel import convert,gauge
import pytest

def test_integer():
    assert convert('1/4') == 25
    assert convert('0/4') == 0
    assert convert('4/4') == 100

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

def test_valid_type():
    with pytest.raises(ValueError):
        convert('three/four')


def test_gauge():
    assert gauge(.75) == 'E'
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'
    assert gauge(45) == '45%'
    assert gauge(105) == 'F'
    assert gauge(0) == 'E'

if __name__ == "__main__":
    main()
