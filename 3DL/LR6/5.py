class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            # Преобразуем отрицательный индекс: -1 → 0, -2 → 1, -3 → 2 и т.д.
            new_index = -index - 1
            # Проверяем чтобы не выйти из за границы
            if new_index >= len(self):
                raise IndexError("Индекс за пределами списка")
            return super().__getitem__(new_index)
        else:
            # Положительные индексы и срезы — работают как обычно
            return super().__getitem__(index)
# Пример 
sl = SmartList([10, 20, 30])
print(sl[0])   #
print(sl[-1]) 
print(sl[-2]) 