import app


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)

#se agrega el siguiente codigo

    def sqrt(self, x):
        self.check_type(x)
        if x < 0:
            raise TypeError("No se puede realizar la raiz cuadrada de un numero negativo")
        return sqrt(x)

    def log10(self, x):
        self.check_type(x)
        if x <= 0:
            raise TypeError("El logaritmo para numeros no positivo no esta definido")
        return log10(x)

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("El parametro debe ser un numero")