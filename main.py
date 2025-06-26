import os

'''
def main() -> None:
    # ...
    pass
'''

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

