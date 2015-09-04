#The name of the fixture again is smtp and you can access its result by listing the name smtp as an input parameter
# in any test or fixture function (in or below the directory where conftest.py is located):

def test_helo(smtp):
    response = smtp.ehlo()
    assert response[0] == 250
    assert "merlinux" in response[1]
    assert 0

def test_noop(smtp):
    response = smtp.noop()
    assert response[0] == 250
    assert 0


