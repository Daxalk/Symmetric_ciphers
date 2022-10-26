def caesar(key, string, action):
    if action == "encrypt":
        sign = 1
    elif action == "decrypt":
        sign = -1
    else:
        return 0
    encryption = []
    for symbol in string:
        encryption.append((ord(symbol) + (key*sign)) % 65536)
    message = ""
    for number in encryption:
        message += chr(number)
    return message


def frequency(text):
    symbols_list = list(set(text))
    freq = {symbol: text.count(symbol) for symbol in symbols_list}
    max_freq = max(freq.values())
    space_index = ''
    for key in freq:
        if freq[key] == max_freq:
            space_index = key
    space_decrypt = ord(' ')
    space_encrypt = ord(space_index)
    key = abs(space_decrypt-space_encrypt)
    message = caesar(key, text, 'decrypt')
    return message


def vigenere(key, string):
    encryption = []
    key_enc = []
    for symbol in string:
        tmp1 = bin(ord(symbol) % 65536)[2::]
        if len(tmp1) < 8:
            encryption.append('0'*(8-len(tmp1)) + tmp1)
        elif len(tmp1) == 8:
            encryption.append(tmp1)
        else:
            return 0

    for symbol in key:
        tmp2 = bin(ord(symbol) % 65536)[2::]
        if len(tmp2) < 8:
            key_enc.append('0'*(8-len(tmp2)) + tmp2)
        elif len(tmp2) == 8:
            key_enc.append(tmp2)
        else:
            return 0

    for i in range(len(encryption)):
        encryption[i] = (encryption[i] and not key_enc[i]) or (not encryption[i] and key_enc[i])



    print(encryption)


def main():
    print("Добро пожаловать в программу!")
    while True:
        try:
            print("1: Шифр Цезаря\n2: Расшифровка шифротекста\n3: Шифр Вернама (XOR-шифр)\n0: Выход из программы")
            print("Введите команду: ")
            command_main = int(input())
            if command_main == 1:
                print("1: Закодировать сообщение\n2: Декодировать сообщение\n3: Вернуться к выбору шифрования")
                command_task = int(input())
                if command_task == 1 or command_task == 2:
                    print("Введите строку:")
                    string = input()
                    print("Введите ключ:")
                    key = int(input())
                    if command_task == 1:
                        message = caesar(key, string, "encrypt")
                    else:
                        message = caesar(key, string, "decrypt")
                    print(f"Полученная строка: {message}")
                elif command_task == 3:
                    pass
                else:
                    print("Такой команды нет!")
            elif command_main == 2:
                print("Введите шифротекст:")
                text = input()
                text = frequency(text)
                print(f"Полученный текст: {text}")
            elif command_main == 3:
                print("Введите строку")
                string = input()
                vigenere('SYSTEM', string)
            elif command_main == 0:
                print("Конец программы!")
                break
        except ValueError:
            print("Некорректный ввод данных")


main()
# fsdl;f;kdsl lflsdlk lfslkdflsdflk vsvs fsf     fdsf fsd   fsd f  fdsfsfdsf    f   s   s
# kxiq@k@pixq%qkqxiqp%qkxqpikqxikqp%{x{x%kxk%%%%%kixk%kxi%%%kxi%k%%kixkxkixk%%%%k%%%x%%%x
