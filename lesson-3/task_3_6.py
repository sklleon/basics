# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    return text.title()

words = []

for word in input('Введите строку заглавными буквами,которые разделены пробелами: ').split(' '):
    words.append(int_func(word))

print(f' Возвращающую слова прописными буквами: {" ".join(words)}')
