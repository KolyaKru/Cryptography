from importlib.resources import path
from typing import final
from stegano import lsb

text = input("Введите шифруемый текст:\n")

key = input("\nВведите ключ:\n")

path_input = "test.bmp"

print("\nШифруемый файл:\n" + path_input)

secret = lsb.hide(path_input, text)

path_output = "out_" + path_input

print("\nТекст зашифрован в файле:\n" + path_output)

secret.save(path_output)

count = 0

while(count != 3):

    key_access = input('\nВведите ключ для расшифровки:\n')

    if (key_access==key):
        final_text = lsb.reveal(path_output)
        print("\nРасшифрованный текст из файла " + path_output + " :\n" + final_text)
        count = 3
    else:
        count = count + 1
        print("\nНеверный ключ, ещё " + str(3-count) + " попыток(ки)")

