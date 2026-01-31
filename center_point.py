def main(first_x, first_y, second_x, second_y):

    first_distance = first_x ** 2 + first_y ** 2
    second_distance = second_x ** 2 + second_y ** 2

    if first_distance <= second_distance:
        return int(first_x), int(first_y)
    else:
        return int(second_x), int(second_y)

first_dot_x = float(input())
first_dot_y = float(input())
second_dot_x = float(input())
second_dot_y = float(input())

result = main(first_dot_x, first_dot_y, second_dot_x, second_dot_y)

print(f"{result}")
