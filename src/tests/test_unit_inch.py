import unittest
from oxrse_unit_conv.units import inch, m


class TestInch(unittest.TestCase):
    def test_SI(self):
        self.assertTrue(inch.si_unit.matches(m))

    def test_basic_conversion(self):
        self.assertEqual(inch.to_si(1), 0.0254)
        self.assertEqual(inch.to_unit(10, inch), 10)


if __name__ == '__main__':
    unittest.main()
