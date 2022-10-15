import os
import time
from random import randint

from main import main

MINIMAL_NUMBER = -10_000
MAXIMAL_NUMBER = 10_000
NUMBER_OF_RUNS = 10
TEST_FILE_NAME = "out/test.txt"
RESULT_FILE_NAME = "out/result.txt"


def generate_test_file(data_amount):
    generated_data = [str(randint(MINIMAL_NUMBER, MAXIMAL_NUMBER)) for i in range(data_amount)]
    generated_content = " ".join(generated_data)

    with open(TEST_FILE_NAME, "w") as file:
        file.write(generated_content)


amounts_of_test_data = [
    2,
    10,
    100,
    1_000,
    10_000,
    100_000,
    1_000_000,
]


with open(RESULT_FILE_NAME, 'w') as result_file:
    for amount_of_data in amounts_of_test_data:
        average_diff = 0

        for i in range(NUMBER_OF_RUNS):
            generate_test_file(amount_of_data)

            time_before = time.time()
            main(TEST_FILE_NAME)
            time_after = time.time()

            diff = time_after - time_before
            average_diff += diff / NUMBER_OF_RUNS

        result_file.write(f"For amount of data={amount_of_data} program worked for time {average_diff}\n")

try:
    os.remove(TEST_FILE_NAME)
except FileNotFoundError:
    pass
