def parse_values(input_str):
    words = input_str.split()

    values = []

    for word in words:
        if word.lower() == 'true':
            values.append(True)
        elif word.lower() == 'false':
            values.append(False)
        else:
            try:
                values.append(int(word))
            except ValueError:
                try:
                    values.append(float(word))
                except ValueError:
                    values.append(word)

    return values

input_str = input("Enter a string: ")
print(parse_values(input_str))
