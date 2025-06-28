import time
import random

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert_into_tree(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_tree(root.left, value)
    else:
        root.right = insert_into_tree(root.right, value)
    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def binary_tree_sort(numbers):
    if not numbers:
        return []
    root = None
    for num in numbers:
        root = insert_into_tree(root, num)
    result = []
    in_order_traversal(root, result)
    return result

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        numbers = []
        for item in content.split():
            try:
                num = int(item)
                numbers.append(num)
            except ValueError:
                print(f"Предупреждение: '{item}' пропущено (не целое число)")
        return numbers, content

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, numbers)))

def generate_random_numbers(count, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(count)]

def save_numbers_to_file(numbers, filetype="сгенерированных"):
    while True:
        filename = input(f"Введите имя файла для {filetype} чисел (с расширением): ").strip()
        try:
            write_numbers_to_file(filename, numbers)
            print(f"Числа сохранены в {filename}")
            return filename
        except Exception as e:
            print(f"Ошибка: {e}. Попробуйте снова.")

def show_menu():
    print("\nМеню:")
    print("1. Отсортировать данные из файла")
    print("2. Сгенерировать и отсортировать числа")
    print("3. Выход")
    return input("Выберите действие (1-3): ").strip()

def main():
    while True:
        choice = show_menu()

        if choice == '1':
            input_file = input("Введите имя исходного файла (с расширением): ").strip()
            try:
                numbers, original = read_numbers_from_file(input_file)
                print(f"\nИсходные данные: {' '.join(map(str, numbers))}")

                start = time.time()  # Измеряем только время сортировки
                sorted_nums = binary_tree_sort(numbers)
                print(f"Отсортировано: {' '.join(map(str, sorted_nums))}")
                print(f"Время сортировки: {time.time() - start:.6f} сек")  # Выводим время сортировки

                save_numbers_to_file(sorted_nums, "отсортированных")

            except FileNotFoundError:
                print(f"Файл '{input_file}' не найден")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            try:
                count = int(input("Количество элементов: "))
                min_val = int(input("Минимальное значение (целое): "))
                max_val = int(input("Максимальное значение (целое): "))

                numbers = generate_random_numbers(count, min_val, max_val)
                print(f"\nСгенерировано: {' '.join(map(str, numbers))}")

                input_file = save_numbers_to_file(numbers)

                start = time.time()  # Измеряем только время сортировки
                sorted_nums = binary_tree_sort(numbers)
                print(f"Отсортировано: {' '.join(map(str, sorted_nums))}")
                print(f"Время сортировки: {time.time() - start:.6f} сек")  # Выводим время сортировки

                save_numbers_to_file(sorted_nums, "отсортированных")

            except ValueError:
                print("Ошибка: введите целые числа")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == '3':
            print("Выход")
            break

        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()