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
                num = int(item) if '.' not in item else float(item)
                numbers.append(num)
            except ValueError:
                print(f"Предупреждение: значение '{item}' пропущено (не является числом)")
        return numbers, content


def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, numbers)))


def main():
    input_filename = 'unsorted_nums.txt'
    output_filename = 'sorted_nums.txt'
    try:
        numbers, original_content = read_numbers_from_file(input_filename)
        print(f"Исходная строка из файла: '{original_content}'")

        sorted_numbers = binary_tree_sort(numbers)
        print(f"\nРезультат сортировки: {sorted_numbers}")

        write_numbers_to_file(output_filename, sorted_numbers)

    except FileNotFoundError:
        print(f"\nОшибка: Файл '{input_filename}' не найден.")
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")


main()
