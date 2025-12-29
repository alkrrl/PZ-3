def at_encryption():
    al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rev_al = al[::-1]

    message = input("Введите текст для шифрования: ").lower()
    encry_text = ""

    for char in message:
        if char in al:
            index = al.index(char)
            encry_text += rev_al[index]
        else:
            encry_text += char

    print("Зашифрованный текст: {}".format(encry_text))
    return encry_text


def at_decryption():
    al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rev_al = al[::-1]

    message = input("Введите текст для дешифрования: ").lower()
    decry_text = ""

    for char in message:
        if char in rev_al:
            index = rev_al.index(char)
            decry_text += al[index]
        else:
            decry_text += char

    print("Расшифрованный текст: {}".format(decry_text))
    return decry_text


def main():

    while True:
        print("\nМеню:")
        print("1. Шифрование текста")
        print("2. Дешифрование текста")

        try:
            choice = int(input("Выберите действие (1 или 2): "))
        except ValueError:
            print("Ошибка: введите число от 1 до 2")
            continue

        if choice == 1:
            print("\n" + "-" * 20)
            print("Режим шифрования")
            print("-" * 20)
            at_encryption()

        elif choice == 2:
            print("\n" + "-" * 20)
            print("Режим дешифрования")
            print("-" * 20)
            at_decryption()

        else:
            print("Неверный выбор. Введите число от 1 до 2.")


if __name__ == "__main__":
    main()
