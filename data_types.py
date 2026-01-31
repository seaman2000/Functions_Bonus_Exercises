def main(type_, data):

    if type_ == "int":
        return int(data) * 2

    elif type_ == "real":
        return f"{float(data) * 1.5:.2f}"

    elif type_ == "string":
        return f"${data}$"

type_of_input = input()
input_data = input()
result = main(type_of_input, input_data)

print(result)