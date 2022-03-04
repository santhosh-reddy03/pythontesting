import pytest

@pytest.fixture
def fixture_eg():
    print("Inside fixture.")


@pytest.fixture(scope="module", params=['hey', 12])
def fixture_example(request):
    print("Inside fixture. Param: "+str(request.param))

# def test_one(fixture_example):
#     print("test one")


