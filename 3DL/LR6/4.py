import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start_time
        print(f"Время выполнения: {elapsed:.2f} сек")
        # Возвращаем False, чтобы исключение продолжало всплывать
        return False


# Пример
with Timer():
    time.sleep(1.5)