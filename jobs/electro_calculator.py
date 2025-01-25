def calculate_length():
    print("Выберите способ монтажа:")
    print("1. По потолку")
    print("2. По полу")
    print("3. Стандартный монтаж (однопроводная система)")

    option = input("Введите номер способа монтажа: ")
    length = float(input("Введите расстояние между точками в метрах: "))

    if option == '1':
        print(f"Расчет длины проводника по потолку: {length + 10:.2f} метров (учтены дополнительные 10 м на запас).")
    elif option == '2':
        print(f"Расчет длины проводника по полу: {length + 5:.2f} метров (учтены дополнительные 5 м на запас).")
    elif option == '3':
        print(f"Расчет длины проводника для стандартного монтажа: {length:.2f} метров.")
    else:
        print("Неверный выбор.")

def calculate_cross_section():
    print("Выберите группу потребителей:")
    print("1. Освещение")
    print("2. Розетки")
    print("3. Водонагреватели")
    print("4. Отопление")

    option = input("Введите номер группы потребителей: ")
    load = float(input("Введите мощность потребителей в ваттах: "))

    # Простейший расчет сечения, который можно далее улучшить
    if option in ['1', '2']:
        cross_section = load / 10  # Условное значение для освещения и розеток
    elif option == '3':
        cross_section = load / 5   # Условное значение для водонагревателей
    elif option == '4':
        cross_section = load / 8   # Условное значение для отопления
    else:
        print("Неверный выбор.")
        return

    print(f"Необходимое сечение проводника: {cross_section:.2f} мм².")

def calculate_cost():
    material_cost = float(input("Введите стоимость материалов в рублях: "))
    labor_cost = float(input("Введите стоимость работ в рублях: "))
    total_cost = material_cost + labor_cost
    print(f"Общая стоимость работ: {total_cost:.2f} рублей.")

def main():
    while True:
        print("\nВыберите функцию:")
        print("1. Расчет длины проводника")
        print("2. Расчет сечения проводника")
        print("3. Расчет стоимости работ")
        print("4. Выход")

        choice = input("Введите номер функции: ")

        if choice == '1':
            calculate_length()
        elif choice == '2':
            calculate_cross_section()
        elif choice == '3':
            calculate_cost()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()