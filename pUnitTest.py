import unittest

class Temperature:
    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        values = [x for x in [kelvin, celsius, fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('Need argument')

        if len(values) > 1:
            raise ValueError('Only one argument')
        
        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif fahrenheit is not None:
            self.fahrenheit = (fahrenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin
        
        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

class Testing(unittest.TestCase):
    def test(self):
        self.assertTrue(Temperature(0,5,0), f'Temperature = {self.kelvin}'>0)
        return f'Temperature = {self.kelvin} Kelvins'
if __name__=='__main__':
    unittest.main()
