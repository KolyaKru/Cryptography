import numpy
resh = numpy.array([[{1, 2, 3, 1}],
                    [{3, 4, 4, 2}],
                    [{2, 4, 4, 3}],
                    [{1, 3, 2, 1}]])

key = input('Введите ключ:')

word = input('\nВведите слово или несколько слов (без пробелов) из 16 букв: \n')

code_word = ""

if (len(word) == 16):
    code = numpy.array([[word[0], word[5], word[6], word[12]],
                        [word[14], word[15], word[7], word[9]],
                        [word[13], word[3], word[11], word[10]],
                        [word[8], word[2], word[1], word[4]]])

    print('\nЗашифрованная матрица:\n') 
    print(code)

    for i in range(4):
        for j in range(4):
            code_word = code_word + code[i][j]

    print('\nЗашифрованное слово:\n' + code_word)

    #key_access = input('\nВведите ключ для расшифровки:\n')
    
    count = 0

    while(count != 3):

        key_access = input('\nВведите ключ для расшифровки:\n')

        if (key_access==key):
            result = code[0][0] + code[3][2] + code[3][1] + code[2][1] + code[3][3] + code[0][1] + code[0][2] + code[1][2] + code[3][0] + code[1][3] + code[2][3] + code[2][2] + code[0][3] + code[2][0] + code[1][0] + code[1][1]
            print('\nРасшифрованное выражение: \n' + result)
            count = 3
        else:
            count = count + 1
            print("\nНеверный ключ, ещё " + str(3-count) + " попыток(ки)")

else:
    print('Введите больше букв!')
