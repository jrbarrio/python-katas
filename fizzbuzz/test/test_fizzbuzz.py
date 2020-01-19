from fizzbuzz.src.fizzbuzz import fizzbuzz


def test_fizzbuzz_returns_number():
    assert 1 == fizzbuzz(1)
    assert 2 == fizzbuzz(2)
    assert 7 == fizzbuzz(7)


def test_fizzbuzz_returns_fizz_when_multiple_of_three():
    assert 'fizz' == fizzbuzz(3)
    assert 'fizz' == fizzbuzz(6)
    assert 'fizz' == fizzbuzz(9)


def test_fizzbuzz_returns_buzz_when_multiple_of_five():
    assert 'buzz' == fizzbuzz(5)
    assert 'buzz' == fizzbuzz(10)
    assert 'buzz' == fizzbuzz(20)




