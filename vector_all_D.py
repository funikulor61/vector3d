import math

class Vector_all_D:
    def __init__(self, components):
        # Преобразуем входящие данные в кортеж чисел float
        try:
            self.components = tuple(float(x) for x in components)
        except (ValueError, TypeError):
            raise ValueError("Координаты должны быть числами!")

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Размерности векторов не совпадают!")
        return Vector_all_D([self.components[i] + other.components[i] for i in range(len(self))])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Размерности векторов не совпадают!")
        return Vector_all_D([self.components[i] - other.components[i] for i in range(len(self))])

    def __mul__(self, other):
        # Умножение на число (скалярное)
        if isinstance(other, (int, float)):
            return Vector_all_D([x * other for x in self.components])
        # Поэлементное умножение на другой вектор
        elif isinstance(other, Vector_all_D):
            if len(self) != len(other):
                raise ValueError("Размерности для умножения не совпадают!")
            return Vector_all_D([self.components[i] * other.components[i] for i in range(len(self))])
        else:
            raise TypeError("Умножать можно на число или на Vector")

# --- Инициализация данных ---
vectors_dict = {}
print("--- Настройка программы ---")
try:
    n = int(input("Сколько векторов создать? "))
    for i in range(n):
        name = input(f"Введите имя {i+1}-го вектора (например, 'a'): ").strip()
        coords = input(f"Введите координаты через пробел: ").split()
        vectors_dict[name] = Vector_all_D(coords)
except ValueError as e:
    print(f"Ошибка при вводе: {e}")
    exit()

# --- Интерактивное меню ---
print("Доступные операции: + | - | * | exit")
print(f"Ваши векторы: {list(vectors_dict.keys())}")

while True:
    x = input("\nВыберите действие: ").strip().lower()

    match x:
        case "exit":
            print("Завершение работы.")
            break

        case "+":
            name1 = input("Имя 1-го вектора: ")
            name2 = input("Имя 2-го вектора: ")
            try:
                res = vectors_dict[name1] + vectors_dict[name2]
                print(f"Результат сложения: {res}")
            except KeyError:
                print("Ошибка: Вектор не найден.")
            except ValueError as e:
                print(f"Ошибка: {e}")
                
        case "dim":
            name = input("Имя вектора для определения размерности: ")
            if name in vectors_dict:
                # Используем встроенную функцию len(), которая вызовет метод __len__ класса
                dimension = len(vectors_dict[name])
                print(f"Размерность вектора '{name}': {dimension}D")
            else:
                print(f"Ошибка: Вектор '{name}' не найден.")

        case "-":
            name1 = input("Имя 1-го вектора: ")
            name2 = input("Имя 2-го вектора: ")
            try:
                res = vectors_dict[name1] - vectors_dict[name2]
                print(f"Результат вычитания: {res}")
            except KeyError:
                print("Ошибка: Вектор не найден.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        case "*":
            name = input("Имя вектора: ")
            try:
                target = vectors_dict[name]
                print("1. Умножить на число")
                print("2. Умножить на другой вектор (поэлементно)")
                choice = input("Ваш выбор: ")
                
                if choice == "1":
                    val = float(input("Введите число: "))
                    print(f"Результат: {target * val}")
                elif choice == "2":
                    name2 = input("Имя 2-го вектора: ")
                    print(f"Результат: {target * vectors_dict[name2]}")
            except (KeyError, ValueError) as e:
                print(f"Ошибка: {e}")

        case _:
            print("Команда не распознана. Используйте +, -, * или exit.")
