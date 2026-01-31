def sum_previous_numbers(num: int):
    sequence = []

    for i in range(num):
        if i == 0 or i == 1:
            sequence.append(1)
        elif i == 2:
            sequence.append(2)
        else:
            next_number = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
            sequence.append(next_number)

    return sequence

number = int(input())
result = sum_previous_numbers(number)
print(" ".join(str(num) for num in result))