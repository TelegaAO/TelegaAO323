class DatabaseConfig:
 # Хранит единственный экземпляр класса
    _instance = None 
    def __new__(cls, db_name, user, password):
        if cls._instance is None:
            # Создаём объект только при первом вызове
            cls._instance = super().__new__(cls)
            # Сохраняем настройки только один раз
            cls._instance.db_name = db_name
            cls._instance.user = user
            cls._instance.password = password
        # Всегда возвращаем один и тот же экземпляр
        return cls._instance
# Пример
conf1 = DatabaseConfig("shop_db", "admin", "123")
conf2 = DatabaseConfig("users_db", "root", "000")  
print(conf1 is conf2)  
print(conf2.db_name)   