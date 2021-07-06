class Validation:
    @staticmethod
    def input_int(string):
        while True:
            try:
                value = int(input(string))
                return value
            except:
                print("Please type an integer number!!!")

    @staticmethod
    def input_float(string):
        while True:
            try:
                value = float(input(string))
                return value
            except:
                print("Please type a float number!!!")
