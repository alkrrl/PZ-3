al = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

print("1. Зашифровать")
print("2. Расшифровать")

choice = int(input("Выберите (1 или 2): "))

if choice == 1:
    val = input("Введите текст: ")
    key = int(input("Введите ключ (1-32): "))

    val_low = val.lower()
    vald = ""

    for i, letter in enumerate(val_low):
        position = al.find(letter)
        if position != -1:
            new_position = position + key
            new_letter = al[new_position]

            if val[i].isupper():
                vald = vald + new_letter.upper()
            else:
                vald = vald + new_letter
        else:
            vald = vald + val[i]

    print("Зашифрованный текст:", vald)

elif choice == 2:
    val = input("Введите зашифрованный текст: ")
    key = int(input("Введите ключ (1-32): "))

    val_low = val.lower()
    vald = ""

    for i, letter in enumerate(val_low):
        position = al.find(letter)
        if position != -1:
            new_position = position - key
            if new_position < 0:
                new_position = new_position + 33
            new_letter = al[new_position]
            if val[i].isupper():
                vald = vald + new_letter.upper()
            else:
                vald = vald + new_letter
        else:
            vald = vald + val[i]

    print("Расшифрованный текст:", vald)

else:
    print("Неверный выбор")
