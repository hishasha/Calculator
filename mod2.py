def _min(numbers):
    if len(numbers) == 0:
        raise ValueError("list must be not empty")

    min_test = numbers[0]
    for number in range(1, len(numbers)):
        if numbers[number] < min_test:
            min_test = numbers[number]
    return min_test


def _max(numbers):
    if len(numbers) == 0:
        raise ValueError("list must be not empty")

    max_test = numbers[0]
    for number in range(1, len(numbers)):
        if numbers[number] > max_test:
            max_test = numbers[number]
    return max_test


def _sum(numbers):
    # s = 0
    # for item in numbers:
    #     s += item
    # return s
    return 0


def _mult(numbers):
    m = 1
    for item in numbers:
        m *= item
    return m
