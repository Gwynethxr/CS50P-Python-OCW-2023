from bank import value


def main():
    test_value_1()
    test_value_2()

def test_value_1():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('HeLLo') == 0

def test_value_2():
    assert value('Hi') == 20
    assert value('hei') == 20
    assert value('hai') == 20

def test_value_3():
    assert value("What's up?") == 100
    assert value("good morning") == 100

    
if __name__ == "__main__":
    main()