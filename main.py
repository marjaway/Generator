import random
import time
import sys
try:
    import g4f
    import segno
    import banner
    from генератор.bd.person import *
    from генератор.bd.nft_name import *
    from faker import Faker
    from colorama import init
    from colorama import Fore
    init()
except ModuleNotFoundError as mode:
    print(f"Не найден модуль {mode}")
    sys.exit()

faker = Faker("RU_ru")


def main():
    input(Fore.RESET + "\nНажмите Enter чтобы вернуться в меню...")

def fors():
    print(Fore.LIGHTCYAN_EX + "Вы ввели буквы, а надо цифры")

def none():
    print(Fore.CYAN + 'Команда не найдена')

def gpt():
        def ask_gpt(promt:str) -> str:
            responce = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user", "content": promt}],
            )
            return responce
        try:
            if command == "16":
                print(ask_gpt(f"Расскажи анектод, штук так {anekdot}"))
            elif command == "23":
                print(ask_gpt(f"Лучшие сборки на пк, штук так {pc}"))
            elif command == "17":
                print(ask_gpt(f"Пиши на русском, {n}"))
        except ConnectionRefusedError:
            print("Не удалось подключится ( Ошибка: ConnectionRefusedError )")
        main()



while True:
    banner.banner()

    command = input(Fore.CYAN + "\n                                          [ ? ] -> Введите команду: " + Fore.RESET)
    print("\n")

    if command == "1":
        print('''Автор: discord: marjaway
Версия программы -> 0.2.3
Автор не несет ответственности за использование программы! Все сгенерированные данные являются вымышленными!''')
        news = input("\nПоказать историю обновлений (Введите up): ")
        time.sleep(0.1)

        if news == "up":
            time.sleep(0.1)
            print('''
        0.1.0 - Добавлен генератор телефонных номеров и русских имен
        0.1.1 - Добавлена генерация ссылок
        0.1.2 - Переименованы генераторы / Добавлен рандом чисел от 1 до 10
        0.1.3 - Исправления ошибок
        0.1.4 - Добавлены генераторы никнеймов, паролей и почт
        0.1.5 - Добавлен генератор случайных адресов
        0.1.6 - Исправления ошибок / Изменения интерфейса
        0.1.7 - Добавлен генератор городов и профессий
        0.1.8 - Изменен порядок функций / Генератор анекдотов
        0.1.9 - Интеграция ChatGPT
        0.2.0 - Добавлен генератор QR-кодов / Новые функциональные блоки
        0.2.1 - Обновлен генератор QR-кодов / Вынесен интерфейс
        0.2.2 - Добавлены генераторы дат / Генератор решений / Генератор персонажей и названий NFT
        0.2.3 - Добавлено много новый NFT-названий и персонажей в person.py / Переделаны Генартор анектодов, ChatGPT 4 / Добавлен Генератор сборки пк''')
        else:
            none()

        main()
        

    elif command == "2":

        time.sleep(0.2)
        print(Fore.RESET + "\nРандомные числа от 0 до 9999999999\n")
        time.sleep(0.1)
        try:
            randomm = int(input("Сколько чисел хотите вывести: "))
            randomm = int(randomm) 
                
            for h in range(randomm):
                h = random.randint(0, 9999999999)
                print(h)
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "3":

        print(Fore.RESET + "\nГенерация имён\n")
        try:
            name = int(input("Сколько имён хотите сгенерировать: "))
            time.sleep(0.1)
            name = int(name)
                
            for i in range(name):
                print(faker.name())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "4":
        
        time.sleep(0.3)
        print(Fore.RESET + "\nГенерация фамилии")
        try:
            fam = int(input("Количество фамилий: "))
            time.sleep(0.1)
            fam = int(fam)
            for f in range(fam):
                print(faker.last_name())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "5":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенератор личностей...")
        try:
            profe = int(input("\nСколько хотите сгенерировать: "))
            profe = int(profe)
            
            for a in range(profe):
                print("\n")
                print("Имя: " + faker.name())
                time.sleep(0.1)
                print("Адрес: " + faker.address())
                time.sleep(0.1)
                print("Город: " + faker.city())
                time.sleep(0.1)
                print("Страна: " + faker.country())
                time.sleep(0.1)
                print("Работа: " + faker.job())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "6":
        time.sleep(0.2)
        numbers = random.randint(1, 10)
        print(numbers)
        
        main()	
        
            
    elif command == "7":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация банковских карт\n")
        try:
            bank = int(input("Сколько хотите сгенерировать номеров банк. карты: "))
            bank = int(bank)
            for i in range(bank):
                a = random.randint(0000000000000000, 9999999999999999)
                u = random.randint(000, 999)
                print("\n")

                print(a)
                time.sleep(0.1)

                print(u)
                time.sleep(0.1)

                print(faker.name())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "8":
        time.sleep(0.2)
        print(Fore.RESET + "Генерация пароля...\n")
        chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        try:
            number = int(input("Количество паролей: "))
            passw = int(input("Длинна пароля: "))
            print("\n")
            number = int(number)
            passw = int(passw)
            for n in range(number):
                password=''
                for i in range(passw):
                    password += random.choice(chars)
                print(password)
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "9":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация ссылок")
        try:
            web = int(input("\nСколько хотите сгенерировать ссылок: "))
            web = int(web)
                
            for g in range(web):
                print(faker.uri())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "10":
        time.sleep(0.2)
        print(Fore.RESET + "Генератор ников...")
        char = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        try:
            nicks = int(input("\nКоличество ников: "))
            niks1 = int(input("Длинна ника: "))
            print("\n")
            nicks = int(nicks)
            niks1 = int(niks1)
            for p in range(nicks):
                nick=''
                for i in range(niks1):
                    nick += random.choice(char)
                print(nick)
                time.sleep(0.1)
        except ValueError:
            fors()
        main()

    elif command == "11":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация почт...\n")
        try:
            pochta = int(input("Введите количесво почт: "))
            pochta = int(pochta)

            for d in range(pochta):
                print(faker.ascii_free_email())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        

    elif command == "12":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация телефонных номеров...\n")
        try:
            phone = int(input(Fore.CYAN + "Сколько хотите сгенерировать тел.номеров: "))
            phone = int(phone)
            
            for i in range(phone):
                print(faker.phone_number())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        
            
    elif command == "13":
        time.sleep(0.2)
        print(Fore.RESET + "\nРандомайзер улиц\n")
        try:
            ul = int(input("Количество улиц: "))
            ul = int(ul)
            for h in range(ul):
                print(faker.street_address())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
        
            
    elif command == "14":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенератор городов\n")
        try:
            city = int(input("Количество городов: "))
            city = int(city)
            for i in range(city):
                print(faker.city_name())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()
            

    elif command == "15":
        time.sleep(0.2)
        print(Fore.RESET + "\nРандомайзер профессий\n")
        try:
            prof = int(input("Количество профессий: "))
            prof = int(prof)
            for i in range(prof):
                print(faker.job())
                time.sleep(0.1)
        except ValueError:
            fors()
        main()

    elif command == "16":
        print("Надо подождать пока напишет")
        anekdot = input("Сколько надо анекдотов: ")
        gpt()
        

    elif command == "17":
        print("Надо подождать пока напишет")
        n = input("Введите запрос (пишите сразу подробный запрос): ")
        gpt()



    elif command == "18":
        print("Генерация QR-кодов")
        time.sleep(0.3)

        qrcod = input("Введите ссылку для QR-кода: ")
        qrcode = segno.make_qr(f"{qrcod}")

        print('''В каком формате сохранить?
    1. PNG
    2. SVG
    3. PDF''')
        try:
            photo = input("\n[ ? ] - Выберете формат: ")

            if photo == "1":
                qrcode.save("qr-code.png")
            elif photo == "2":
                qrcode.save("qr-code.svg")
            elif photo == "3":
                qrcode.save("qr-code.pdf")
            else:
                print(Fore.BLUE + "Нужно обязательно выбрать формат, в котором сохранится QR-cod")

            print("QR-код был сгенерирован. Сохраняется в папку где находится программа")
        except ValueError:
            fors()
        main()   


    elif command == "19":
        print("Генерация разных дат\n")

        years = random.randint(1, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        hour = random.randint(1, 24)

        print(f"Год - {years}\nМесяц - {month}\nДень - {day}\nЧас - {hour}")
        time.sleep(0.3)

        main()


    elif command == "20":
        while True:
            reshenie = ['Да', 'Нет', 'Наверное']
            dsn = random.choices(reshenie)
            print(dsn)

            input("\nЕще сгенерировать?")
            a = input("\nНапите exit если хотите выйти ( если не хотите выходить, то нажмите Enter): ")
            if a == "exit":
                break


    elif command == "21":
        try:
            random_person = int(input("Сколько нужно: "))
            random_person = int(random_person)
            for i in range(random_person):
                random_person = random.choices(list)
                print(random_person)
                time.sleep(0.1)
        except ValueError:
            fors()
        main()


    elif command == "22":
        try:
            nft_random = int(input("Количество ( названия могут повторяться ): "))
            nft_random = int(nft_random)
            for i in range(nft_random):
                random_nft = random.choices(nft_list)
                print(random_nft)
                time.sleep(0.1)
        except ValueError:
            fors()
        main()

    elif command == "23":
        print("Надо подождать пока напишет")
        pc = input("Сколько надо сборок: ")
        gpt()

    elif command == "24":
        time.sleep(0.1)
        print("Завершение работы программы...")
        break 

    else:
        none()
        main()