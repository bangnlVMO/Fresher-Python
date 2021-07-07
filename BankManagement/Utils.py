def input_int(string):
    while True:
        try:
            value = int(input(string))
            return value
        except ValueError:
            print("Please type an integer!!!")


def input_float(string):
    while True:
        try:
            value = float(input(string))
            return value
        except ValueError:
            print("Please type an float!!!")