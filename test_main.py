import sys
from io import StringIO
from unittest import TestCase, main

import main as my_program

TEST_FILE_NAME = "out/test.txt"
test_list = [-55, 7, -30, -2, 23]
test_result = """
Мин: -55
Макс: 23
Произведение: -531300
Сумма: -57
"""


class MainTest(TestCase):
    def test_main(self):
        test_content = " ".join(str(item) for item in test_list)

        with open(TEST_FILE_NAME, "w") as file:
            file.write(test_content)

        real_stdout = sys.stdout
        fake_stdout = StringIO()
        sys.stdout = fake_stdout

        my_program.main(TEST_FILE_NAME)

        sys.stdout = real_stdout

        result = fake_stdout.getvalue()

        self.assertEqual(result.strip(), test_result.strip())


if __name__ == "__main__":
    main()
