import sys

def min_moves_to_equalize(nums):

    nums.sort()
    median = nums[len(nums) // 2]  # Выбираем медиану в качестве целевого значения

    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python task4.py input_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = []
    try:
        with open(input_file, 'r') as f:
            for line in f:
                nums.append(int(line.strip()))
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        sys.exit(1)
    except ValueError:
        print(f"Ошибка: Некорректные данные в файле '{input_file}'. Ожидаются целые числа.")
        sys.exit(1)

    result = min_moves_to_equalize(nums)
    print(result)