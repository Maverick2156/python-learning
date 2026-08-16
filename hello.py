# Спрашивает имя
#name = input("What's your name?").strip().title()

# Убирает пробелы в начале и конце строки
#name = name.strip().title()

# Делает первую букву заглавной, а остальные строчными
#name = name.title()

# Делает первую букву заглавной, а остальные строчными
#name = name.title

# Разделяет имя на первую и последнюю части
#first, last = name.split(" ")

# Говорит приветствие
#print(f"hello, {first} {last}!")

# def этот ключевое слово, которое используется для определения функции в Python.
#def hello(to="World"):
#    print("Hello", to)

from os import name


def main():
    #hello()  # Вызывает функцию hello без аргументов, поэтому используется значение по умолчанию "world"
    name = input("What's your name? ")
    hello(name)
    #print(name)


def hello(to="World"):
    print("Hello", to)

main()  # Вызывает функцию main, которая запускает программу


scope # Это ключевое слово, которое используется для определения области видимости переменных в Python. В данном случае, оно используется для определения области видимости переменной name внутри функции main() и функции hello().