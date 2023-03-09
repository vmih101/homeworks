class Math:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def addition(self):
        result = self.a + self.b
        return print(result)

    def multiplication(self):
        result = self.a * self.b
        return print(result)

    def division(self):
        result = self.a / self.b
        return print(result)

    def subtraction(self):
        result = self.a * self.b
        return print(result)


def main():
    expression = Math(10, 40).multiplication()

if __name__ == '__main__':
    main()