import sys

def circular_path(n, m):
  
    arr = list(range(1, n + 1))
    result = []
    start_idx = 0  
    current_pos = 0  

    while True:
        result.append(arr[current_pos])
        next_position = (current_pos + m - 1) % len(arr)

        if next_position == start_idx:
            break

        current_pos = next_position

    return ''.join(map(str, result))  

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py <n> <m>")
        sys.exit(1)  # Завершаем программу, если передано неверное количество аргументов

    try:
        n = int(sys.argv[1])  # Преобразуем первый аргумент в целое число
        m = int(sys.argv[2])  # Преобразуем второй аргумент в целое число
    except ValueError:
        print("Error: n and m must be integers.")
        sys.exit(1)  # Завершаем программу, если аргументы не являются целыми числами

    # Вызываем функцию с полученными значениями
    result = circular_path(n, m)

    if result:
      print(result)
    else:
        print("No solution found.")
