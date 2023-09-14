from twttr import shorten


def main():
    test_shorten_cases()

def test_shorten_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('tWiTtER') == 'tWTtR'
    assert shorten ("23") == "23"
    assert shorten('heLLO, WOorld') == 'hLL, Wrld'


if __name__ == "__main__":
    main()