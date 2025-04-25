import random
from tqdm import tqdm
from faker import Faker
import time
import g4f
import segno
from colorama import init
from colorama import Fore, Back, Style
init()


for i in tqdm(range(100), desc="Загрузка"):
    time.sleep(0.03)


faker = Faker("RU_ru")


print(Fore.CYAN + '''\n				  █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█ - version 0.1.9
				  █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄''')
				  

while True:
    print(Fore.RESET + '''
	   					  ║
						  ║
	  					  ║	 
	 ╔════════════════════════════════════════╬══════════════════════════════════════╗
	 ║					  ║           				 ║
	 ║  					  ║					 ║
	 ║ Генератор           		Генерация для интернета   	      Другое     ║
 ╔════════════════════════════════╗ ╔════════════════════════════════╗ ╔═════════════════════════════════╗
 ║ [ 1 ] - Информация о софте 	  ║ ║ [ 7 ] - Генератор банк. карт   ║ ║ [ 13 ] - Генератор улиц 	 ║
 ║ [ 2 ] - Рандомайзер цифр       ║ ║ [ 8 ] - Генератор паролей      ║ ║ [ 14 ] - Генератор городов      ║
 ║ [ 3 ] - Генератор ру имён	  ║ ║ [ 9 ] - Генератор ссылок	     ║ ║ [ 15 ] - Генератор профессий    ║
 ║ [ 4 ] - Генератор фамилий	  ║ ║ [ 10 ] - Генератор ников       ║ ║ [ 16 ] - Генератор анекдотов	 ║
 ║ [ 5 ] - Генератор личностей	  ║ ║ [ 11 ] - Генератор почт	     ║ ║ [ 17 ] - ChatGPT 4	 	 ║
 ║ [ 6 ] - Рандомайзер от 1 до 10 ║ ║ [ 12 ] - Генератор тел.номеров ║ ║ [ 18 ] - Генератор QR-кодов     ║
 ╚════════════════════════════════╝ ╚════════════════════════════════╝ ╚═════════════════════════════════╝
 ╔═════════════════════════════════╗╔═════════════════════════════════╗╔═════════════════════════════════╗
 ║ [ 19 ] - Выход из программы     ║║                                 ║║                                 ║  
 ║                                 ║║                                 ║║                                 ║
 ║                                 ║║                                 ║║                                 ║                     
 ║                                 ║║                                 ║║                                 ║
 ║                                 ║║                                 ║║                                 ║
 ╚═════════════════════════════════╝╚═════════════════════════════════╝╚═════════════════════════════════╝''')


    command = input(Fore.CYAN + "					[ ? ] -> Введите число: " + Fore.RESET)
    print("\n")

    if command == "1":
        print('''	Автор tg: @marjaway / discord: marjaway
	Версия софта -> 0.2.0
	Автор не несёт ответственность за эту программу :). Всё что генерирует программа это вымошленно!
	Также прога может крашить после использование функции! ( в скором времени это будет исправлено )''')
        news = input("\nПосмотреть историю обновлений (Напиши update): ")
        time.sleep(0.1)

        if news == "update":
            time.sleep(0.1)
            print('''
        0.1.0 - Добавлено Генератор тел. номеров / Генератор ру имён
        0.1.1 - Исправленно много багов / Добавлен Генерациая ссылок
        0.1.2 - Изменение названий генераторам / Добавлен Рандомайзер чисел от 1 до 10
        0.1.3 - Исправление багов
        0.1.4 - Добавлен Генератор ников / Генератор паролей / Генератор почт
        0.1.5 - Добавлен Генератор рандом улиц
        0.1.6 - Исправление багов / Изменение названий / Изменения интерфейса
        0.1.7 - Добавлен Генератор городов / Генератор профессий
        0.1.8 - Добавление загрузки при заходе в программу / Изменён порядок функций / Генератор анекдотов
        0.1.9 - Добавлен ChatGPT
        0.2.0 - Добавлен Генератор QR-кодов / Добавлены новые блоки функций''')

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню\n")
        

    elif command == "2":
        time.sleep(0.2)
        print(Fore.RESET + "\nРандомные числа от 0 до 9999999999\n")
        time.sleep(0.1)
        randomm = input("Сколько чисел хотите вывести: ")
        randomm = int(randomm) 
            
        for h in range(randomm):
            h = random.randint(0, 9999999999)
            print(h)
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню...")
        

    elif command == "3":
        print(Fore.RESET + "\nГенерация имён\n")
        name = input("Сколько имён хотите сгенерировать: ")
        time.sleep(0.1)
        name = int(name)
            
        for i in range(name):
            print(faker.name())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "4":
        time.sleep(0.3)
        print(Fore.RESET + "\nГенерация фамилии")
        
        fam = input("Количество фамилий: ")
        time.sleep(0.1)
        fam = int(fam)
        for f in range(fam):
            print(faker.last_name())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "5":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенератор личностей...")
        profe = input("\nСколько хотите сгенерировать: ")
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

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "6":
        time.sleep(0.2)
        numbers = random.randint(1, 10)
        print(numbers)
        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")	
        
            
    elif command == "7":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация банковских карт\n")
        m = input("Сколько хотите сгенерировать номеров банк. карты: ")
        m = int(m)
        for i in range(m):
            a = random.randint(0000000000000000, 9999999999999999)
            u = random.randint(000, 999)
            print("\n")
            print(a)
            time.sleep(0.1)
            print(u)
            time.sleep(0.1)
            print(faker.name())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "8":
        time.sleep(0.2)
        print(Fore.RESET + "Генерация пароля...\n")
        chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        number = input("Количество паролей: ")
        length = input("Длинна пароля: ")
        print("\n")
        number = int(number)
        length = int(length)
        for n in range(number):
            password=''
            for i in range(length):
                password += random.choice(chars)
            print(password)
            time.sleep(0.1)
        
        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "9":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация ссылок")
        web = input("\nСколько хотите сгенерировать ссылок: ")
        web = int(web)
            
        for g in range(web):
            print(faker.uri())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "10":
        time.sleep(0.2)
        print(Fore.RESET + "Генератор ников...")
        char = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        nnumber = input("\nКоличество ников: ")
        llengeth = input("Длинна ника: ")
        print("\n")
        nnumber = int(nnumber)
        llengeth = int(llengeth)
        for p in range(nnumber):
            nick=''
            for i in range(llengeth):
                nick += random.choice(char)
            print(nick)
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")

    elif command == "11":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация почт...\n")
        numbber = input("Введите количесво почт: ")
        numbber = int(numbber)

        for d in range(numbber):
            print(faker.ascii_free_email())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "12":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенерация телефонных номеров...\n")
        phone = input(Fore.CYAN + "Сколько хотите сгенерировать тел.номеров: ")
        phone = int(phone)
        
        for i in range(phone):
            print(faker.phone_number())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        
            
    elif command == "13":
        time.sleep(0.2)
        print(Fore.RESET + "\nРандомайзер улиц\n")
        ul = input("Количество улиц: ")
        ul = int(ul)
        for h in range(ul):
            print(faker.street_address())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        
            
    elif command == "14":
        time.sleep(0.2)
        print(Fore.RESET + "\nГенератор городов\n")
        city = input("Количество городов: ")
        city = int(city)
        for i in range(city):
            print(faker.city_name())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню") 
        

    elif command == "15":
        time.sleep(0.2)
        print(Fore.RESET + "\nРандомайзер профессий\n")
        prof = input("Количество профессий: ")
        prof = int(prof)
        for i in range(prof):
            print(faker.job())
            time.sleep(0.1)

        input(Fore.RESET + "\nНажмите Enter, чтобы вернуться в меню")
        

    elif command == "16":
        print("Привет, расскажи какой-нибудь анекдот\n")
        def ask_gpt(promt:str)->str:
            responce = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user", "content": promt}],
            )
            return responce
        print(ask_gpt(f"Расскажи анекдот "))
        input("Нажмите Enter, чтобы вернуться в меню...")
        

    elif command == "17":
        n = input("Введите запрос (пишите сразу подробный запрос): ")
        def ask_gpt(promt:str)->str:
            responce = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user", "content": promt}],
            )
            return responce
        print(ask_gpt(f"Пиши на русском, {n}"))
        input("Нажмите Enter, чтобы вернуться в меню")


    elif command == "18":
        print("Генерация QR-кодов")
        time.sleep(0.3)

        qrcod = input("Введите ссылку для QR-кода: ")
        qrcode = segno.make_qr(f"{qrcod}")
        print("QR-код был сгенерирован. Сохраняется в папку где находится программа")
        qrcode.save("qr-code.png") 

        input("Нажмите Enter, чтобы вернуться в меню")   


    elif command == "19":
        time.sleep(0.1)
        print("Выход из программы...")
        break 
        

    else:
        print(Fore.BLUE + "Ненайдена такая комманда8")
        input(Fore.RESET + "Нажмите Enter, чтобы продолжить")