from Python_Testing.calculator import addition,subtraction 

def test_addition(): 
    assert addition(10,10) == 20
    assert addition(5,5) == 10
    assert addition(100,33478923742389) == 33478923742489

# assert statement allows us to establish whether the test has passed or failed by asserting certain states of the code. 
def test_subtraction(): 
    assert subtraction(1,1) == 0
