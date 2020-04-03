import pytest

@pytest.fixture(params=[1,2,3,4,5,6])
def aa(request):
    a= request.param
    print("初始",a)
    def qw():
        print("55555")
    request.addfinalizer(qw)
class Test_a():
    def test_rr(self,aa):
        print("======={}======")

# @pytest.fixture()
# def bb():
#     return 56
# d = [1,2,3,4,5,6]
# @pytest.mark.parametrize("value",d)
# @pytest.mark.parametrize("aa","1",indirect=True)
# def test_q(value,aa):
#     print("value：",value)
#     print("aa:",aa)
