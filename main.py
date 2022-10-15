from mod2 import _mult, _max, _sum, _min


def main(filename):
    with open(filename, encoding='utf-8') as file:
        line = file.readline()
        numbers = [int(i) for i in line.split()]

    print('Мин:', _min(numbers))
    print('Макс:', _max(numbers))
    print('Произведение:', _mult(numbers))
    print('Сумма:', _sum(numbers))


if __name__ == '__main__':
    main(input('Введите имя файла: '))
