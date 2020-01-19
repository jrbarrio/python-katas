from fizzbuzz.src.fizzbuzz import fizzbuzz


def test_fizzbuzz_returns_number():
    assert 1 == fizzbuzz(1)
    assert 2 == fizzbuzz(2)
    assert 7 == fizzbuzz(7)
