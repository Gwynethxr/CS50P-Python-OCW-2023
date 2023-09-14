from plates import is_valid


def main():
    test_min_andmax()
    test_unique_simbol()
    test_start_two_letter()
    test_start_middlenumber()
    test_first_number()


def test_min_andmax():
    assert is_valid("AA") == True
    assert is_valid("ZXCV55") == True
    assert is_valid("Z") == False
    assert is_valid ("MLKJHOPS") == False

def test_start_two_letter():
    assert is_valid("AA") == True
    assert is_valid('A2') == False
    assert is_valid('55') == False
    assert is_valid('9S') == False

def test_start_middlenumber():
    assert is_valid("CS50") == True
    assert is_valid("CCC555") == True
    assert is_valid("CKK55A") == False

def test_first_number():
    assert is_valid("CS052") == False
    assert is_valid("CS552") == True

def test_unique_simbol():
    assert is_valid ("CS50@#") == False
    assert is_valid ("C@502") == False

if __name__ == "__main__":
    main()