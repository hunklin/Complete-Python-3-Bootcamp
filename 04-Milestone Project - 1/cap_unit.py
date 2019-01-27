import unittest
import cap


class CapUnit(unittest.TestCase):  # CamelCase
    def test_one(self):  # snake case
        text = "hunk"
        result = cap.to_cap(text)
        self.assertEqual(result, "Hunk")

    def test_two(self):
        text = 'hello hunk'
        result = cap.to_cap(text)
        self.assertEqual(result, 'Hello Hunk')


if __name__ == '__main__':
    unittest.main()
