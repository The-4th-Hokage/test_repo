import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive_test
@pytest.mark.parametrize('StringToCapitalize,ResultString', 
                         [('просто текст', 'Просто текст'), 
                          ('Просто текст', 'Просто текст'), 
                          ('', ''),
                          (' ', ' ')])
def test_capitalize_positive(StringToCapitalize, ResultString):
    res = string_utils.capitalize(StringToCapitalize)
    assert res == ResultString


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('NotString', 
                         [(12521356), 
                          [34634,],
                          (236.457),
                          {'Key': 'Value'}, 
                          ()])
def test_capitalize_negative(NotString):
    with pytest.raises(TypeError):
        res = string_utils.capitalize(NotString)


@pytest.mark.positive_test
@pytest.mark.parametrize('StringToTrim, ResultString', 
                         [(' Пробел в начале', 'Пробел в начале'),
                          ('Пробел в конце ', 'Пробел в конце '),
                          ('Безпробелов', 'Безпробелов')])
def test_trim_positive(StringToTrim, ResultString):
    res = string_utils.trim(StringToTrim)
    assert res == ResultString


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('NotString', 
                         [(12352365),
                          (135.45678),
                          [2346],
                          {'key': 'value'},
                          (),
                          (None)])
def test_trim_negative(NotString):
    with pytest.raises(TypeError):
        res = string_utils.trim(NotString)


@pytest.mark.positive_test
@pytest.mark.parametrize('StringToContains, FindSymbol',
                         [('Ищем строковую букву', 'т'),
                          ('Ищем заглавную букву', 'И'),
                          ('Ищем пробел', ' '),
                          ('Ищем запятую,', ','),
                          ('Ищем цифру 1', '1',),
                          ('Ищем спец символ №', '№'),
                          ('Ищем 2 буквы', 'ем')])
def test_contains_positive(StringToContains, FindSymbol):
    res = string_utils.contains(StringToContains, FindSymbol)
    assert res == True


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('NotString, FindSymbol', 
                         [([2, 5,6,346,34673,77], '2'),
                          ({'key': 'value'}, 'v'),
                          ((),()),
                          ([], []),
                          ({}, {}),
                          (236236, '6'),
                          (235.6, '3')])
def test_contains_negative(NotString, FindSymbol):
    with pytest.raises(TypeError):
        res = string_utils.contains(NotString, FindSymbol)


@pytest.mark.positive_test
@pytest.mark.parametrize('StringToDeleteSymbol, SymbolToDelete, Result_String', [('Удаляем один строчный символ', 'о', 'Удаляем дин стрчный симвл'),
                                                                                 ('Удаляем один заглавный символ', 'У', 'даляем один заглавный символ'),
                                                                                 ('Удаляем два строчных символа', 'дв', 'Удаляем а строчных символа'),
                                                                                 ('УДаляем два заглавных символа', 'УД', 'аляем два заглавных символа'),
                                                                                 ('Удаляем спец № символ %', '№', 'Удаляем спец  символ %'),
                                                                                 ('Удаляем цифры 24697362 из текста', '2', 'Удаляем цифры 469736 из текста'),
                                                                                 ('Удаляем знак, препинания', ',', 'Удаляем знак препинания')])
def test_delete_symbol_positive(StringToDeleteSymbol, SymbolToDelete, Result_String):
    res = string_utils.delete_symbol(StringToDeleteSymbol, SymbolToDelete)
    assert res == Result_String


@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('StringToDeleteSymbol, SymbolToDelete', [((), 'g'),
                                                     ([], 't'),
                                                     ({}, 'h'),
                                                     (122152356, 'q'),
                                                     (1235.4567, 'u'),
                                                     ({'key': 'value'}, 'b'),
                                                     ('Строка на вход', 2363246),
                                                     ('Строка на вход', 2356.2345),
                                                     ('Строка на вход', []),
                                                     ('Строка на вход', {'key': 'value'}),
                                                     ('Строка на вход', ()),
                                                     ('Строка на вход', None),])
def test_delete_symbol_negative_not_string(StringToDeleteSymbol, SymbolToDelete):
    with pytest.raises(TypeError):
        res = string_utils.delete_symbol(StringToDeleteSymbol, SymbolToDelete)