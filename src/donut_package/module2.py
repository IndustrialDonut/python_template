"""This is an auxillery module"""

class MyClass:
    """My class does nothing all too"""

    def __init__(self, x) -> None:
        """Ctor"""
        self.a = 5
        self.b = x
    

    def something(self):
        """Print x + a and return 0"""
        print(self.a + self.b)
        return 0