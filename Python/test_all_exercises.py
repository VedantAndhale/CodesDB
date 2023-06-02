import unittest

from exercises.bigger_guy import bigger_guy
from exercises.three_sum import three_sum

class AllTests(unittest.TestCase):
    def test_bigger_guy(self):
      print('\n\n---------------')
      print('🛠️ Function 👉 bigger_guy()')
      assert bigger_guy(1, 2) == 2
      assert bigger_guy(10, 20) == 20
      assert bigger_guy(20, 10) == 20
      assert bigger_guy(10, 10) == 10
      print('\nAll Tests Passed (4/4) ✅')
      print('---------------')

    def test_three_sum(self):
      print('\n\n---------------')
      print('🛠️ Function 👉 three_sum()')
      assert three_sum(1, 2, 3) == 5
      print('\nAll Tests Passed (4/4) ✅')
      print('---------------')

if __name__ == '__main__':
    unittest.main()