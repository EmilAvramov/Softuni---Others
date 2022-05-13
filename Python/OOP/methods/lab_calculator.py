class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        list_args = args
        result = list_args[0]
        for i in list_args[1:]:
            result *= i
        return result

    @staticmethod
    def divide(*args):
        list_args = args
        result = args[0]
        for i in list_args[1:]:
            result /= i
        return result

    @staticmethod
    def subtract(*args):
        list_args = args
        result = list_args[0]
        for i in list_args[1:]:
            result -= i
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
