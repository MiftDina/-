import random

# Блок с функциями
def service_help():
    print("-----ПРАВИЛА ИГРЫ-----")
    print("1. Необходимо догадаться, что за слово скрывается за символами *")
    print("2. В зависимости от сложности, у Вас будет 15, 10 или 5 попыток отгадать слово")
    print("3. Попыткой считается неверно приведённый вариант слова или буква, которая отсутствует в отгадываемом слове")
    print("4. Слово можно отгадывать по буквам или пытаться угадать целиком")
    print("5. П","\n")
    print("-----СПИСОК КОМАНД-----")
    print("!help  -  показать правила и список команд")
    print("!again  -  сдаться, начать сначала")
    print("!advice  -  подсказка, откроется скрытая буква")
    print("!health  -  узнать оставшееся колическтво попыток")
    print("!letters  -  вывод всех использованных в данной игре букв")
    print("!end   -  закончить игру","\n")

# Наборы слов
name_level = ["Легко", "Средне", "Сложно"]
name_collect = ["Животные", "Столицы", "Реки России", "Профессии"]
kollect_animal = ["зебра", "слон", "крокодил", "собака", "гуанако", "лошадь", "макак", "марал", "мартышка", "медведь", "бобёр", "тушканчик", "осёл", "выдра", "мышь", "кошка", "норка", "опоссум", "утконос", "сурикат", "панда", "орангутанг", "кенгуру", "носорог"]
kollect_capital = ["Москва", "Каир", "Анкара", "Амстердам", "Афины", "Белград", "Берн", "Прага", "Хельсинки", "Братислава", "Брюссель", "Будапешт", "Бухарест", "Вадуц", "Валлетта", "Варшава", "Ватикан", "Вена", "Вильнюс", "Дублин", "Загреб", "Киев", "Кишинёв", "Копенгаген", "Лиссабон", "Лондон", "Любляна", "Люксембург", "Мадрид", "Минск", "Монако", "Москва", "Осло", "Париж", "Рим"]
kollect_river = ["Енисей", "Волга", "Днепр", "Хатанга", "Лена", "Дунай", "Иртыш", "Колыма", "Вилюй", "Ангара", "Кама", "Индигирка", "Клязьма", "Пехорка", "Шерна"]
kollect_proffesion = ["инженер", "хирург", "пожарный", "учитель", "дизайнер", "журналист", "ветеринар", "бухгалтер", "автомеханик", "токарь", "кинолог", "кондитер", "косметолог", "машинист", "парикмахер", "переводчик", "программист", "режиссёр", "следователь", "сварщик", "экономист", "юрист", "электрик"]
all_collect = [kollect_animal, kollect_capital, kollect_river, kollect_proffesion]

# Алфавит
alphabet_1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Второстепенные массивы
phrases = ["Нет такой буквы!", "Повезёт в следующий раз!", "Хорошая попытка, но этой буквы нет.", "Ваш выбор не дал положительного резуьтата."]
say_yes = ["ДА", "да", "Да", "дА", "ага", "yes", "YES", "Yes"]


print("Добро пожаловать в игру <ПОЛЕ ЧУДЕС>")
service_help()
flag_end = 1
health = 0

#Основной цикл
while flag_end:
    print("-----НАЧНЁМ НОВУЮ ИГРУ!-----")

    #Выбор сложности
    print("Легко")
    print("Средне")
    print("Сложно")
    choice_level = input("Выберите сложность: ")
    if choice_level == "!end":
        print("\n", "-----ИГРА ЗАКОНЧЕНА-----", sep="")
        flag_end = 0
    else:
        if not choice_level in name_level:
            if choice_level == "!again":
                print("Сдаться и начать сначала можно только после выбора сложности и слова.")
            elif choice_level == "!advice":
                print("Получить подсказку можно только после выбора сложности и слова.")
            elif choice_level == "!health":
                print("Узнать оставшееся колическтво попыток можно только после выбора сложности и слова.")
            elif choice_level == "!letters":
                print("Увидеть использованные буквы можно только после выбора сложности и слова.")
            elif choice_level == "!help":
                service_help()
            elif choice_level == "!end":
                flag_end = 0
                print("\n","-----ИГРА ЗАКОНЧЕНА-----",sep = "")
                break
            while flag_end:
                choice_level = input("Не корректно введена сложность, попробуйте ещё раз: ")
                if choice_level in name_level:
                    print("Сложность выбрана успешно.","\n")
                    break
                elif choice_level == "!again":
                    print("Сдаться и начать сначала можно только после выбора сложности и слова.")
                elif choice_level == "!advice":
                    print("Получить подсказку можно только после выбора сложности и слова.")
                elif choice_level == "!health":
                    print("Узнать оставшееся колическтво попыток можно только после выбора сложности и слова.")
                elif choice_level == "!letters":
                    print("Увидеть использованные буквы можно только после выбора сложности и слова.")
                elif choice_level == "!help":
                    service_help()
                elif choice_level == "!end":
                    flag_end = 0
                    print("\n","-----ИГРА ЗАКОНЧЕНА-----",sep = "")
                    break
        else:
            print("Сложность выбрана успешно.","\n")

    if flag_end == 1:
        #Выбор категории слова
        print("Категории:")
        quantity_collect = len(name_collect)
        for i in range(1,quantity_collect+1):
            print(i,".",name_collect[i-1]," [",len(all_collect[i-1]),"]",sep="")
        print("[В скобках указано количество доступных слов в категории]")
        choice_kollect = input("Введите категорию слова: ")
        if choice_kollect == "!end":
            print("\n", "-----ИГРА ЗАКОНЧЕНА-----", sep="")
            flag_end = 0
        else:
            if not choice_kollect in name_collect:
                if choice_kollect == "!again":
                    print("Сдаться и начать сначала можно только после выбора слова.")
                elif choice_kollect == "!advice":
                    print("Получить подсказку можно только после выбора слова.")
                elif choice_kollect == "!health":
                    print("Узнать оставшееся колическтво попыток можно только после выбора слова.")
                elif choice_kollect == "!letters":
                    print("Увидеть использованные буквы можно только после выбора слова.")
                elif choice_kollect == "!help":
                    service_help()
                elif choice_kollect == "!end":
                    flag_end = 0
                    print("\n","-----ИГРА ЗАКОНЧЕНА-----",sep = "")
                    break
                while flag_end:
                    choice_kollect = input("Не корректно введена категория слова, попробуйте ещё раз: ")
                    if choice_kollect in name_collect:
                        print("Отличный выбор!")
                        break
                    elif choice_kollect == "!again":
                        print("Сдаться и начать сначала можно только после выбора слова.")
                    elif choice_kollect == "!advice":
                        print("Получить подсказку можно только после выбора слова.")
                    elif choice_kollect == "!health":
                        print("Узнать оставшееся колическтво попыток можно только после выбора слова.")
                    elif choice_kollect == "!letters":
                        print("Увидеть использованные буквы можно только после выбора слова.")
                    elif choice_kollect == "!help":
                        service_help()
                    elif choice_kollect == "!end":
                        flag_end = 0
                        print("\n","-----ИГРА ЗАКОНЧЕНА-----",sep = "")
                        break
            else:
                print("Отличный выбор!")

    if flag_end == 1:
        # Категория слова выбрана успешно, выбор случайного слова из коллекции:
        number_collect = 0
        for j in name_collect:
            if j == choice_kollect:
                break
            else:
                number_collect += 1
        word = random.choice(all_collect[number_collect])
        all_collect[number_collect].remove(word)
        # Выбор слова завершён, слово удалено из массива.

        # Выбор количества попыток угадать букву в зависимости от сложности
        if choice_level == "Легко":
            health = 15
        elif choice_level == "Средне":
            health = 10
        else:
            health = 5

        # Алгоритм угадывания букв
        print("\n", "=================================")
        word_len = len(word)
        word_star = word_len * ["*"]
        letters_input = ""
        total = 0  # Количество угаданных букв
        counter = 0 # Количество попыток

        while flag_end:
            if health == 0:
                print("К сожалению, у Вас не удалось угадать слово и Вы проиграли. ")
                print("Загаданное слово:", word,"\n")
                final = input("Для того, чтобы сыграть новую игру, нужно ввести <да>: ")
                if final == "!again":
                    print("Не время сдаваться! Лучше сыграйте ещё раз.")
                elif final == "!advice":
                    print("Получить подсказку можно только после выбора слова.")
                elif final == "!health":
                    print("Узнать оставшееся колическтво попыток можно только после выбора слова.")
                elif final == "!letters":
                    print("Увидеть использованные буквы можно только после выбора слова. Мы вопспринимаем ")
                elif final == "!help":
                    service_help()
                elif final == "!end":
                    flag_end = 0
                    print("\n","-----ИГРА ЗАКОНЧЕНА-----",sep = "")
                elif not final in say_yes:
                    flag_end = 0
                    print("\n", "-----ИГРА ЗАКОНЧЕНА-----", sep="")

                break
            else:
                if health == 1:
                    print("Осторожно! Осталась последняя попытка!")

                print("Слово :", word_star)
                letter = input("Ваша буква или слово целиком: ")
                if ((letter in alphabet_1) or (letter in alphabet_2)) and (letter != "\n") and (letter != ""): # Если буква из русского алфавита
                    # Перевод регистра буквы М -> м
                    if letter in alphabet_2:
                        number_letter = 0
                        for k in alphabet_2:
                            if k == letter:
                                break
                            else:
                                number_letter += 1
                        letter = alphabet_1[number_letter]
                    else:
                        number_letter = 0
                        for k in alphabet_1:
                            if k == letter:
                                break
                            else:
                                number_letter += 1

                    if letter in letters_input:
                        print("Такую букву Вы уже вводили. Чтобы увидеть список введённых букв введите команду !letters")
                    else:
                        counter += 1
                        letters_input = letters_input + " " + letter
                        if (alphabet_1[number_letter] in word) or (alphabet_2[number_letter] in word):
                            quantity_letter = word.count(alphabet_1[number_letter]) + word.count(alphabet_2[number_letter])
                            if (quantity_letter == 1) or (quantity_letter >= 5):
                                print("Поздравляем! В этом слове буква", "<" + letter + ">", "встречается", quantity_letter, "раз")
                            else:
                                print("Поздравляем! В этом слове буква", "<" + letter + ">", "встречается", quantity_letter, "раза")
                            for l in range(0,word_len):
                                if word[l] == alphabet_1[number_letter]:
                                    word_star[l] = alphabet_1[number_letter]
                                if word[l] == alphabet_2[number_letter]:
                                    word_star[l] = alphabet_2[number_letter]
                            total += quantity_letter
                            if total == word_len:
                                break
                        else:
                            # Если не угадали букву
                            health -= 1
                            if health != 0:
                                print(random.choice(phrases))
                else:
                    # Если буква не из русского алфавита или это не буква
                    if letter == "!again":
                        print("Вы приняли решение сдаться и начать сначала.")
                        print("Загаданное слово:", word, "\n")
                        break
                    elif letter == "!advice":
                        print("Всем иногда нужна помощь!")
                        mass_advice = ""
                        for p in range(0, word_len):
                            if word_star[p] == "*":
                                mass_advice = mass_advice + word[p]
                        letter_advice = random.choice(mass_advice)

                        if letter_advice in alphabet_2:
                            number_letter = 0
                            for k in alphabet_2:
                                if k == letter_advice:
                                    break
                                else:
                                    number_letter += 1
                            letter_advice = alphabet_1[number_letter]
                        else:
                            number_letter = 0
                            for k in alphabet_1:
                                if k == letter_advice:
                                    break
                                else:
                                    number_letter += 1
                        print("Откройте букву: ", letter_advice)

                        if (alphabet_1[number_letter] in word) or (alphabet_2[number_letter] in word):
                            quantity_letter = word.count(alphabet_1[number_letter]) + word.count(alphabet_2[number_letter])
                            if (quantity_letter == 1) or (quantity_letter >= 5):
                                print("Поздравляем! В этом слове буква", "<" + letter_advice + ">", "встречается", quantity_letter, "раз")
                            else:
                                print("Поздравляем! В этом слове буква", "<" + letter_advice + ">", "встречается", quantity_letter, "раза")
                            for l in range(0,word_len):
                                if word[l] == alphabet_1[number_letter]:
                                    word_star[l] = alphabet_1[number_letter]
                                if word[l] == alphabet_2[number_letter]:
                                    word_star[l] = alphabet_2[number_letter]
                            total += quantity_letter
                            if total == word_len:
                                break

                    elif letter == "!health":
                        print("Оставшееся колическтво попыток:",health)
                    elif letter == "!letters":
                        print("Использованные Вами буквы: ", letters_input)
                    elif letter == "!help":
                        service_help()
                    elif letter == "!end":
                        flag_end = 0
                        print("\n","-----ИГРА ЗАКОНЧЕНА-----",sep = "")
                        break
                    elif letter == word:
                        print("Невероятно! Вы назвали слово целиком!")
                        counter += 1
                        word_star = word
                        total = word_len
                        break
                    else:
                        print("Не корректно введена буква или не правильно названо слово!")
                        health -= 1
                        counter += 1

        # Проверка на угаданное слово
        if (total == word_len) and (word_star.count("*") == 0):
            print("\n","ПОЗДРАВЛЯЕМ! Вы угадали слово: ", word, sep = "")
            print("Колличество попыток:", counter, "\n")
            final = input("Для того, чтобы сыграть новую игру, нужно ввести <да>: ")

            if final == "!again":
                print("Не время сдаваться! Лучше сыграйте ещё раз.")
            elif final == "!advice":
                print("Получить подсказку можно только после выбора слова.")
            elif final == "!health":
                print("Узнать оставшееся колическтво попыток можно только после выбора слова.")
            elif final == "!letters":
                print("Увидеть использованные буквы можно только после выбора слова. Мы вопспринимаем ")
            elif final == "!help":
                service_help()
            elif final == "!end":
                flag_end = 0
                print("\n", "-----ИГРА ЗАКОНЧЕНА-----", sep="")
                break
            elif not final in say_yes:
                flag_end = 0
                print("\n", "-----ИГРА ЗАКОНЧЕНА-----", sep="")
                break
