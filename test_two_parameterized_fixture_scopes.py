import pytest

@pytest.fixture(scope="module", params = ['mod1', 'mod2'])
def modarg(request):
    param = request.param
    print ('create', param)
    def fin():
        print ('fin %s' %param)
    return param

@pytest.fixture(scope='function', params=[1,2])
def otherarg(request):
    return request.param

def test_0(otherarg):
    print ("  test0", otherarg)

def test_1(modarg):
    print ("  test1",modarg)

def test_2(otherarg, modarg):
    print ("  test2", otherarg, modarg)


