class Mathematics:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def substract(self):
        return self.x - self.y

    def divide(self):
        if self.y == 0:
            raise ValueError('Cannot divide by zero')
        return self.x / self.y

    def multiplication(self):
        return self.x * self.y