from app import greet
def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("") == "Hello, !"

def test_greet_with_special_characters():
    assert greet("John Doe") == "Hello, John Doe!"
    assert greet("!@#$%^&*()") == "Hello, !@#$%^&*()!"
    assert greet("12345") == "Hello, 12345!"