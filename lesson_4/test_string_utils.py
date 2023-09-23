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
def test_capitalize_and_remove_empty(date, result):
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


@pytest.mark.parametrize('string, symbol',[
    ('SkyPro', 'S'),
    ('Привет', 'р')
    ])       
def test_contains_positive(string, symbol):
    utils = StringUtils()
    res = utils.contains(string, symbol)
    assert res == True
    
@pytest.mark.parametrize('string, symbol', [
    ('SkyPro', 's'),
    ('Привет', 'я')
    ])       
def test_contains_negative(string, symbol):
    utils = StringUtils()
    res = utils.contains(string, symbol)
    assert res == False
 

@pytest.mark.xfail(strict=True)
def test_to_list_positive(string, delimiter, result):
    utils = StringUtils()
    res = utils.to_list(string, delimiter)
    assert res == result
    