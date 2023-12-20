import unittest
from figure import figure

class TestParalelogram(unittest.TestCase):

    def test_area(self):
        lenght = 3

        whidth = 2

        height = 4
        p = figure(lenght,whidth, height)
        result = p.area()
        self.assertAlmostEqual(result, 52)
    def test_volume(self):
        lenght = 3

        whidth = 2

        height = 4
        p = figure(lenght,whidth, height)
        result = p.volume()
        self.assertAlmostEqual(result, 24)



if __name__ == '__main__':
    unittest.main()
