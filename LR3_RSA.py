import rsa

message = (input("Введите шифруемое выражение:\n")).encode('utf8')

pubkey, privkey = rsa.newkeys(512) # Генерируем 2 ключа
print('\nГенерируем 2 ключа...')
print('\nПубличный ключ: \n' + ((str(pubkey)).replace(')', "")).split("(")[1])
print('\nПриватный ключ: \n' + ((str(privkey)).replace(')', "")).split("(")[1])

cipher = rsa.encrypt(message, pubkey) # Шифруем
print('\nЗашифрованное выражение: \n' + str(cipher))

mess = rsa.decrypt(cipher, privkey) # Расшифровываем
print('\nРасшифрованное выражение: \n' + mess.decode('utf8'))