from proj.sample_module import add
import pytest

"""
Pytest Fixtures

    pytest has xUnit-style of fixtures.

    setup_module and teardown_module are module level fixtures.

    setup_class and teardown_class are class level fixtures. These fixtures need to be decorated with @classmethod.

    setup_method and teardown_method are method level fixtures.

    setup_function and teardown_function are function level fixtures.

    Apart from these fixtures, pytest also supports defining customised fixtures and using it for a specific method or function.

    to share the fixtures between different test files and subdirectories, create fixtures inside conftest.py file

    with pytest-xdist we get run on parallel cpus using pytest -n cpus, and pytest -f will rereun failed test cases

"""
@pytest.mark.skip('testing fixture')
class TestAdd:

    def test_add(self):
        assert 7 == add(3,4)
    
    def test_neg_add(self):
        assert -1 == add(3, -4)
    
# pytest fixture
# TODO :: create pytest fixture
# @pytest.mark.skip() decorator skips a test case or class
# @pytest..mark.skipif((condition, reason)) skips based on condition

def test_using_raise():
    with pytest.raises(TypeError):
        add(2,'2') == 4


@pytest.fixture()
def fixture_ex():
    print("\nbefore test")
    yield 10
    print("\nend of test")

@pytest.fixture(scope='class')
def fix_class():
    print("class fixture")

def testfix(fixture_ex):
    print("inside test")
    assert 10 == fixture_ex

# temp_path_factory to create temporary directories
# temp_path_factory.mktemp()

class Test_Fixtue:


    # to use mutliple fixture at once
    @pytest.mark.usefixtures('fix_class', 'fixture_ex')
    def test_one(self):
        print("inside class fix")
        assert 'a' == 'A'.lower()


@pytest.fixture(params=[1,2,3])
def param_fixture(request):
    print("\nfixture_parmas_{}".format(request.param))

def test_params(param_fixture):
    assert "a" == "a"

# alternate way to parameterize
@pytest.mark.parametrize("val, out", [(2,4), (3,9)])
def test_sq(val, out):
    print("val*val=out({val}*{val}={out})".format(val=val, out=out))
    assert val*val == out
