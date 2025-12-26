class Frange:
    def __init__(self, start, stop, step):
        if step == 0:
            raise ValueError("step cannot be zero")
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        # Каждый новый цикл for начинает с начала
        return FrangeIterator(self.start, self.stop, self.step)
class FrangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step
    def __next__(self):
        # Для положительного шага: останавливаемся, когда current >= stop
        # Для отрицательного шага: останавливаемся, когда current <= stop
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        else:
            if self.current <= self.stop:
                raise StopIteration
        value = self.current
        self.current += self.step
        return value
# Пример
for x in Frange(1, 3, 0.5):
    print(x)