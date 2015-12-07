class SimpleCalculator(object):
    def __init__(self, param1, param2):
        self.fn = None
        self.param1 = param1
        self.param2 = param2

    def addition(self):
        return self.param1 + self.param2

    def subtraction(self):
        return self.param1 - self.param2

    def multiplication(self):
        return self.param1 * self.param2

    def division(self):
        return self.param1 / self.param2
