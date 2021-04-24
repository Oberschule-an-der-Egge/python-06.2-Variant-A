import main

homer = main.Homer()
homer2 = main.Homer()
homer3 = main.Homer()
homer4 = main.Homer()
homer5 = main.Homer()


class TestBasic:

    def test_class_homer(self):
        assert homer.name == 'Homer'
        assert homer.city == 'Springfield'
        assert homer.age == 39

    def test_class_homer_do_chores(self):
        method = getattr(homer, 'do_chores')
        assert callable(method)

    def test_hammock_returns_list(self):
        result = main.magic_hammock(homer)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_hammock_returns_clone(self):
        result = main.magic_hammock(homer)
        assert isinstance(result[0], main.Homer)
        assert result[0] is homer
        assert isinstance(result[1], main.Homer)

    def test_clone_chores(self):
        original, clone = main.magic_hammock(homer)
        assert original.do_chores() == 'Nope!'
        assert clone.do_chores() == 'Ok!'


class TestBonus:

    def test_hammock_returns_multiple_homers(self):
        result = main.magic_hammock(homer, homer2, homer3, homer4, homer5)
        assert len(result) == 10
        assert homer in result
        for element in result:
            assert isinstance(element, main.Homer)
    
    def test_hammock_returns_flanders(self):
        flanders = main.Flanders()
        result = main.magic_hammock(flanders)
        
        assert len(result) == 2
        assert isinstance(result[0], main.Flanders)
        assert result[0] is flanders
        assert isinstance(result[1], main.Flanders)
        
    def test_hammock_returns_multiple_flanders(self):
        flanders = main.Flanders()
        flanders2 = main.Flanders()
        flanders3 = main.Flanders()
        result = main.magic_hammock(flanders, flanders2, flanders3)
        assert len(result) == 6
        assert flanders in result
        for element in result:
            assert isinstance(element, main.Flanders)
        
