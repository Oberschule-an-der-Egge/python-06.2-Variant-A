import main

homer = main.Homer()
homer2 = main.Homer()
homer3 = main.Homer()
homer4 = main.Homer()
homer5 = main.Homer()


def test_class_homer():
    assert homer.name == 'Homer'
    assert homer.city == 'Springfield'
    assert homer.age == 39


def test_hammock_returns_list():
    result = main.magic_hammock(homer)
    assert isinstance(result, list)
    assert len(result) == 2


def test_hammock_returns_clone():
    result = main.magic_hammock(homer)
    assert isinstance(result[0], main.Homer)
    assert result[0] is homer
    assert isinstance(result[1], main.Homer)


def test_hammock_returns_multiples():
    result = main.magic_hammock(homer, homer2, homer3, homer4, homer5)
    assert len(result) == 10
    for element in result:
        assert isinstance(element, main.Homer)


def test_clone_chores():
    original, clone = main.magic_hammock(homer)
    assert original.do_chore() == 'Nope!'
    assert clone.do_chore() == 'Ok!'
