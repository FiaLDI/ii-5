#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Поиск файлов с определённым типом данных. В файловой системе есть
# как текстовые, так и бинарные файлы. Найдите все текстовые файлы ( ASCII
# или UTF-8 ), начиная с уровня 3, и проверьте их содержимое. Поиск ограничен
# глубиной 20 уровней


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


def is_text_file(content):
    """
    Проверяет, является ли содержимое текстовым (ASCII или UTF-8).
    """
    try:
        content.decode("utf-8")  # Пробуем декодировать в UTF-8
        return True
    except (UnicodeDecodeError, AttributeError):
        return False


def search_text_files(node, current_level=1, max_depth=20, start_level=3):
    """
    Ищет текстовые файлы в дереве, начиная с уровня start_level и ограничиваясь max_depth.
    """
    if current_level > max_depth:  # Ограничение глубины поиска
        return []

    results = []
    if current_level > start_level:  # Проверяем узлы только начиная с start_level
        if isinstance(node.value, bytes) and is_text_file(node.value):
            results.append((node, node.value.decode("utf-8")))

    # Рекурсивно проверяем детей, независимо от текущего уровня
    for child in node.children:
        results.extend(
            search_text_files(child, current_level + 1, max_depth, start_level)
        )

    return results


def main():
    # Создание дерева с глубиной и разнообразным содержимым
    root = TreeNode(b"Root data")
    # Уровень 1
    child1 = TreeNode(b"This is a text file.")
    child2 = TreeNode(b"\x89PNG some binary content")
    child3 = TreeNode(b"Binary data here")
    # Уровень 2
    child1_1 = TreeNode(b"Another text file at level 2.")
    child1_2 = TreeNode(b"Yet another text file.")
    child2_1 = TreeNode(b"\x00\xFF Binary file again")
    child3_1 = TreeNode(b"Level 2 text data.")

    # Уровень 3 (глубина начала анализа)
    child1_1_1 = TreeNode(b"This text is at level 3.")
    child1_1_2 = TreeNode(b"\xDE\xAD\xBE\xEF Still binary content")
    child1_2_1 = TreeNode(b"Level 3 valid UTF-8 text.")
    child3_1_1 = TreeNode(b"Text deep in level 3.")

    # Уровень 4
    child1_1_1_1 = TreeNode(b"Deeper text in level 4.")
    child1_2_1_1 = TreeNode(b"Some more text at level 4.")
    child3_1_1_1 = TreeNode(b"Binary\x00 data in level 4")

    # Построение дерева
    root.add_children(child1, child2, child3)
    child1.add_children(child1_1, child1_2)
    child2.add_child(child2_1)
    child3.add_child(child3_1)
    child1_1.add_children(child1_1_1, child1_1_2)
    child1_2.add_child(child1_2_1)
    child3_1.add_child(child3_1_1)
    child1_1_1.add_child(child1_1_1_1)
    child1_2_1.add_child(child1_2_1_1)
    child3_1_1.add_child(child3_1_1_1)

    # Поиск текстовых файлов с уровня 3
    text_files = search_text_files(root, start_level=3)

    # Печать результатов
    print("Найденные текстовые файлы с уровня 3:")
    for node, content in text_files:
        print(f"Node: {node}, Content: {content}")


if __name__ == "__main__":
    main()
