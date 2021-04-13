import main

def test_parser():
    input = '5'
    assert main.parse(input) == [5]


def test_parser_1():
    input = '1 2'
    assert main.parse(input) == [12]


def test_parser_2():
    input = '1 2 3 + 4 5 6 ='
    assert main.parse(input) == [123, '+', 456, '=']


def test_parser_3():
    input = '1 2 3 - 2 3 ='
    assert main.parse(input) == [123, '-',23, '=']


def test_parser_4():
    input = '1 0 - 1 0 0 ='
    assert main.parse(input) == [10, '-', 100, '=']


def test_parser_5():
    input = '1 0 * 2 2 ='
    assert main.parse(input) == [10, '*', 22, '=']


def test_parser_6():
    input = '1 0 0 / 3 ='
    assert main.parse(input) == [100, '/', 3, '=']


def test_parser_7():
    input = '9 / 1 0 ='
    assert main.parse(input) == [9, '/', 10, '=']


def test_parser_8():
    input = '1 2 3 +'
    assert main.parse(input) == [123, '+']


def test_parser_9():
    input = '1 2 3 + 4'
    assert main.parse(input) == [123, '+', 4]


def test_parser_10():
    input = '1 2 3 + 4 5 6'
    assert main.parse(input) == [123, '+', 456]


def test_calc():
    input = '1 0 0 / 3 ='
    assert main.calculation(main.parse(input)) == 33


def test_calc_1():
    input = ''
    assert main.calculation(main.parse(input)) == 0


def test_calc_2():
    input = '5'
    assert main.calculation(main.parse(input)) == 5


def test_calc_3():
    input = '1 2'
    assert main.calculation(main.parse(input)) == 12


def test_calc_4():
    input = '1 2 3 + 4 5 6 ='
    assert main.calculation(main.parse(input)) == 579


def test_calc_5():
    input = '1 2 3 - 2 3 ='
    assert main.calculation(main.parse(input)) == 100


def test_calc_6():
    input = '1 0 - 1 0 0 ='
    assert main.calculation(main.parse(input)) == -90


def test_calc_7():
    input = '1 0 * 2 2 ='
    assert main.calculation(main.parse(input)) == 220


def test_calc_8():
    input = '9 / 1 0 ='
    assert main.calculation(main.parse(input)) == 0


def test_calc_9():
    input = '1 2 3 +'
    assert main.calculation(main.parse(input)) == 123


def test_calc_10():
    input = '1 2 3 + 4'
    assert main.calculation(main.parse(input)) == 4


def test_calc_11():
    input = '1 2 3 + 4 5 6'
    assert main.calculation(main.parse(input)) == 456