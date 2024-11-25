#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Рассмотрим задачу поиска информации в иерархических структурах данных,
# например, в файловой системе, где каждый каталог может содержать подкаталоги
# и файлы. Алгоритм итеративного углубления идеально подходит для таких задач,
# поскольку он позволяет исследовать структуру данных постепенно, углубляясь на
# один уровень за раз и возвращаясь, если целевой узел не найден. Для этого
# необходимо:
# Построить дерево, где каждый узел представляет каталог в файловой
# системе, а цель поиска — определенный файл.
# Найти путь от корневого каталога до каталога (или файла), содержащего
# искомый файл, используя алгоритм итеративного углубления.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"


def iterative_deepening_search(root, target):
    depth = 0
    while True:
        found = depth_limited_search(root, target, depth)
        if found is not None:
            return found
        depth += 1


def depth_limited_search(node, target, depth):
    if depth == 0 and node.value == target:
        return node.value
    if depth > 0:
        for child in node.children:
            result = depth_limited_search(child, target, depth - 1)
            if result is not None:
                return result
    return None


def main():
    # Создаем дерево каталогов
    root = TreeNode("root")
    folder1 = TreeNode("folder1")
    folder2 = TreeNode("folder2")
    file1 = TreeNode("file1.txt")
    file2 = TreeNode("file2.txt")

    folder1.add_children(file1)
    root.add_children(folder1, folder2)

    # Ищем файл
    target_file = "file1.txt"
    result = iterative_deepening_search(root, target_file)

    if result:
        print(f"Файл '{target_file}' найден: {result}")
    else:
        print(f"Файл '{target_file}' не найден.")


if __name__ == "__main__":
    main()
