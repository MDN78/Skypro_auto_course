import pytest
from string_utils import StringUtils

utils = StringUtils()

    
@pytest.mark.parametrize('date, result', [
    ('skypro', 'Skypro'), 
    ('SKYPRO', 'Skypro'),
    ('sKyPrO', 'Skypro'),
    ('скайпро', 'Скайпро'),
    ('  skypro', 'skypro'),
    ('  второй', 'второй'),
    (' Sky Pro', 'Sky Pro')
    ])
def test_capitalize_or_trim(date, result):
    utils = StringUtils()
    if date[0] == ' ':
        print("Start testing function 'Remove empty'")
        res = utils.trim(date)
        assert res == result
    else:
        print("Start testing function 'Capitalize'")
        res = utils.capitilize(date)
        assert res == result


@pytest.mark.parametrize('string, symbol', [
    ('SkyPro', 'S'),
    ('Proverka', 'a'),
    ('Second', 's'),
    ('sos', 's'),
    ('Проверка', 'П'),
    ('Вторая', 'я'),
    ('1234', '1')
    ])
def test_start_or_end_with(string, symbol):
    utils = StringUtils()
    if string[0] == symbol:
        print("Start testing function 'starts_with")
        res = utils.starts_with(string, symbol)
        assert res == True
    elif string[-1] == symbol:
        print("Start testing function 'end_with")
        res = utils.end_with(string, symbol)
        assert res == True


@pytest.mark.parametrize('string, symbol, result',[
    ('SkyPro', 'S', True),
    ('Привет', 'р', True),
    ('SkyPro', 's', False),
    ('Привет', 'я', False),
    ('Sky Pro', 'P', True),
    pytest.param(111, 3, False, marks=pytest.mark.xfail)
    ])       
def test_contains(string, symbol, result):
    utils = StringUtils()
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, delimiter', [
    ('"a, b, c", ","', '["a", "b", "c"]' ),
    ('""')])
@pytest.mark.xfail
def test_to_list_positive(string, delimiter, result):
    utils = StringUtils()
    res = utils.to_list(string, delimiter)
    assert res == result


@pytest.mark.parametrize('string, result', [
    (" ", True),
    ("", True),
    ("Skypro", False),
    ("Привет", False),
    ('12345', False)
])   
def test_is_empty_positive(string, result):
    utils = StringUtils()
    res = utils.is_empty(string)
    assert res == result

   
@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("Привет", "П", "ривет"),
    ("test", "", "test"),
    pytest.param(121, 2, 11, marks=pytest.mark.xfail),
    ("", "", "")
])
def test_delete_symbol(string, symbol, result):
    utils = StringUtils()
    res = utils.delete_symbol(string, symbol)
    assert res == result

   
@pytest.mark.parametrize('list, joiner, result', [
    ([1,2,3,4], ", ", "1, 2, 3, 4"),
    ([], "", ""),
    (['a', 'b', 'c'], "*", "a*b*c" )
])
def test_list_to_string(list, joiner, result):
    utils = StringUtils()
    res = utils.list_to_string(list, joiner)
    assert res == result
    