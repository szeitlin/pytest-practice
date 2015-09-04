import pytest

@pytest.fixture
def smtp():
    import smtplib
    return smtplib.SMTP("merlinux.edu")

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert 0

