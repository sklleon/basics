# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(text):
    return text.upper()

words = []

for word in input('Введите строку прописными буквами,которые разделены пробелами: ').split(' '):
    words.append(int_func(word))

print(f' Возвращающую слова заглавными буквами: {" ".join(words)}')

