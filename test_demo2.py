

def test_firstProgram(setup):
    msg = "Hi"
    assert msg == "Hi", "Test fail because string do not match"

def test_secondProgram(setup):
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"
