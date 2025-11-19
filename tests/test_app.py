from src.app import greet

def test_greet():
    print("Function returned:", greet("DevOps"))
    assert greet("DevOps") == "Hello DevOps!"
