"""This is the main example module where we have a class that does nothing"""

import configparser

class Adder:
    """This is a class that holds a function to add one"""

    def __init__(self) -> None:
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        self.parser = parser
        

    def add_one(number):
        """Return number + 1"""
        return number + 1


    def get_config(self):
        return self.parser