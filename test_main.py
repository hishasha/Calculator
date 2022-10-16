import sys
import unittest

from io import StringIO

import main as my_program
from constants import TEST_FILE_NAME, TEST_LIST, TEST_RESULT


class MainTest(unittest.TestCase):
    def test_main(self):
        test_content = " ".join(str(item) for item in TEST_LIST)

        with open(TEST_FILE_NAME, "w") as file:
            file.write(test_content)

        real_stdout = sys.stdout
        fake_stdout = StringIO()
        sys.stdout = fake_stdout

        my_program.main(TEST_FILE_NAME)

        sys.stdout = real_stdout

        result = fake_stdout.getvalue()

        self.assertEqual(result.strip(), TEST_RESULT.strip())


if __name__ == "__main__":
    unittest.main()
