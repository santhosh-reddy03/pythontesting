import pytest

def test_one(fixture_eg):
    print("Inside test one.")
    assert "hello" == "HELLO".lower()


@pytest.mark.parametrize("val,out", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square_it(val, out):
    print('{}*{}: '.format(val, val)+str(val*val))
    assert val*val == out



@pytest.fixture
def make_record():
    def _make_record(name):
        return {
            "name": name,
            "qty" : 0
        }
    return _make_record

def test_one(make_record):
    o1 = make_record("John")
    o2 = make_record("Jane")
    print(o1)
    print(o2)

CONTENT = "content"
def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT


def compute_large_data():
    return "SOME LARGE TEXT DATA......"

@pytest.fixture(scope="session")
def large_data(tmp_path_factory):
    data = compute_large_data() #Some text data is generated here
    d = tmp_path_factory.mktemp("data_needed")
    p = d / "data.txt"
    p.write_text(data)
    return p

def test_one(large_data):
    d = large_data
    print(d.read_text())