import sys
import math

def calculate_position(center_x, center_y, circle_radius, point_x, point_y):
    distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)

    if distance == circle_radius:
        return 0
    elif distance < circle_radius:
        return 1
    else:
        return 2

def solve():

    try:
        with open(sys.argv[1], 'r') as circle_file:
            center_x, center_y = map(float, circle_file.readline().split())
            circle_radius = float(circle_file.readline())

        with open(sys.argv[2], 'r') as points_file:
            points_count = 0
            for line in points_file:
                point_x, point_y = map(float, line.split())

                points_count += 1
                if points_count > 100:
                    print("Error: Too many points in points file (maximum 100 allowed).")

                position = calculate_position(center_x, center_y, circle_radius, point_x, point_y)
                print(position)

    except FileNotFoundError:
        print("Error: One or more files not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file> <points_file>")
        sys.exit(1)

    solve()
