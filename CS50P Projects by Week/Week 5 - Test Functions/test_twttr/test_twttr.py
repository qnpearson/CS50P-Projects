from twttr import shorten

#Call Test Functions
def main():
    test_lower()
    test_upper()
    test_number()


#Test Lower
def test_lower():
    assert shorten("twitter") == "twttr"

#Test Upper
def test_upper():
    assert shorten("TWITTER") == "TWTTR"

#Test numbers
def test_number():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("CS.twt") == "CS.twt"

if __name__ == "__main__":
    main()