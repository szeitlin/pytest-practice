import pytest
import smtplib

@pytest.fixture(scope="module",
                params = ['merlinux.edu', 'mail.python.org'])
def smtp(request):
    smtp = smtplib.SMTP(request.param)
    def fin():
        print ("teardown smtp")
        smtp.close()
    request.addfinalizer(fin)
    return smtp

# fixture finalization / executing teardown code
# pytest supports execution of fixture specific finalization code when the fixture goes out of scope. 
# By accepting a request object into your fixture function you can call its request.addfinalizer one or multiple times
# Extending the previous example, we can flag the fixture to create two smtp fixture instances 
# which will cause all tests using the fixture to run twice. The fixture function gets access to each parameter 
# through the special request object:

# pytest will build a string that is the test ID for each fixture value in a parametrized fixture, 
# e.g. test_ehlo[merlinux.eu] and test_ehlo[mail.python.org] in the above examples. 
# These IDs can be used with -k to select specific cases to run, 
# and they will also identify the specific case when one is failing. 
# Running pytest with --collect-only will show the generated IDs.

