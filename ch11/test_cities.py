import unittest

from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Does 'Venice, Italy' work?"""
        location = city_country('venice', 'italy')
        self.assertEqual(location, 'Venice, Italy')

    def test_city_country_population(self):
        """Does 'Lawrence, Kansas - 100000' work?"""
        address = city_country('Lawrence', 'Kansas', 100000)
        self.assertEqual(address, 'Lawrence, Kansas - 100000')

if __name__ == '__main__':
    unittest.main()
    

