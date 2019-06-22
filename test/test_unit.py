import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.name = "daniel"
        print "hello"

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print self.name
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_eq(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
