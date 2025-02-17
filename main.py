import random
from faker import Faker
import time
from colorama import init
from colorama import Fore, Back, Style
init()


faker = Faker("RU_ru")

print(Fore.CYAN + "\n				█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█")
print("				█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄")
print("\n")

print(Fore.RESET + '''   						  ║
						  ║
	  					  ║	 
	 ╔════════════════════════════════════════╬══════════════════════════════════════╗
	 ║					  ║           				 ║
	 ║  					  ║					 ║
	 ║ Генерация личности          Генерация для интернета    	      Другое     ║
 ╔════════════════════════════════╗ ╔════════════════════════════════╗ ╔════════════════════════════════╗
 ║ [ 1 ] - Информация о софте 	  ║ ║ [ 7 ] - Генератор банк. карт   ║ ║ [ 11 ] - Рандомайзер от 1 до 10║
 ║ [ 2 ] - Генератор тел.номеров  ║ ║ [ 8 ] - Генератор паролей      ║ ║ [ 12 ] - Рандомайзер цифр      ║
 ║ [ 3 ] - Генератор ру имён	  ║ ║ [ 9 ] - Генератор ссылок	     ║ ║ [ 13 ] - Генератор улиц        ║
 ║ [ 4 ] - Генератор фамилий	  ║ ║ [ 10 ] - Генератор ников       ║ ║ [ 14 ] - Выход из софта        ║
 ║ [ 5 ] - Генератор личностей	  ║ ║ by marjaway		     ║ ║ 				║
 ║ [ 6 ] - Генератор почт	  ║ ║	  version - 0.1.9	     ║ ║				║
 ╚════════════════════════════════╝ ╚════════════════════════════════╝ ╚════════════════════════════════╝''')


command = input(Fore.CYAN + "					[ ? ] -> Введите число: " + Fore.RESET)
print("\n")


if command == "1":
	print(Fore.RESET + "\nАвтор tg: @marjaway / discord: marjaway")
	time.sleep(0.2)
	print("Версия софта -> 0.1.8\n")
	time.sleep(0.2)
	print("Автор не несёт ответственность за эту программу :). Всё что генерирует программа это вымошленно!")
	time.sleep(0.2)
	print("Также прога может крашить после использование функции! \n")
	time.sleep(0.2)
	news = input("\nПосмотреть историю обновлений ( Напиши update ): ")
	time.sleep(0.2)
	print("\n")

	if news == "update":
		time.sleep(0.2)
		print("0.1.0 - Добавлено Генератор тел. номеров / Генератор ру имён")
		time.sleep(0.2)
		print("0.1.1 - Исправленно много багов / Добавлено Генерацию ссылок")
		time.sleep(0.2)
		print("0.1.2 - Изменение названий генераторам / Добавлено Рандомайзер чисел от 1 до 10")
		time.sleep(0.2)
		print("0.1.3 - Исправление багов")
		time.sleep(0.2)
		print("0.1.4 - Добавлено Генератор ников / Генератор паролей / Генератор почт\n")
		time.sleep(0.2)
		print("\n0.1.5 - Сделана версия софта для телефона")
		time.sleep(0.2)
		print("0.1.6 - Добавлено Генератор рандом улиц")
		time.sleep(0.2)
		print("0.1.7 - Исправление багов")
		time.sleep(0.2)
		print("0.1.8 - Изменения названий")
		time.sleep(0.2)
		print("0.1.9 - Изменения интерфейса")
		time.sleep(0.2)

		input("\nНажмите Enter, чтобы выйти..")


if command == "2":
	time.sleep(0.2)

	print(Fore.RESET + "\nГенерация телефонных номеров...\n")

	phone = input("Сколько хотите сгенерировать тел.номеров: ")
	phone = int(phone)
	
	for i in range(phone):
		print(faker.phone_number())
		time.sleep(0.5)

	input("\nНажмите Enter, чтобы выйти..")
		

if command == "7":
	time.sleep(0.2)

	print(Fore.RESET + "\nГенерация банковских карт\n")

	m = input("Сколько хотите сгенерировать номеров банк. карты: ")
	m = int(m)
	for i in range(m):
		a = random.randint(0000000000000000, 9999999999999999)
		u = random.randint(000, 999)
		print("\n")
		print(a)
		time.sleep(0.2)
		print(u)
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")


if command == "5":
	time.sleep(0.2)

	print(Fore.RESET + "\nГенератор личностей...")

	profe = input("\nСколько хотите сгенерировать: ")
	profe = int(profe)
	
	for a in range(profe):
		print("\n")
		print("Имя: " + faker.name())
		time.sleep(0.2)
		print("Адрес: " + faker.address())
		time.sleep(0.2)
		print("Город: " + faker.city())
		time.sleep(0.2)
		print("Страна: " + faker.country())
		time.sleep(0.2)
		print("Работа: " + faker.job())
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")
		
		
if command == "6":
	time.sleep(0.2)

	print(Fore.RESET + "\nГенерация почт...\n")

	numbber = input("Введите количесво почт: ")
	numbber = int(numbber)

	for d in range(numbber):
		print(faker.ascii_free_email())
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")

		
if command == "9":
	time.sleep(0.2)

	print(Fore.RESET + "\nГенерация ссылок")

	web = input("\nСколько хотите сгенерировать ссылок: ")
	web = int(web)
		
	for g in range(web):
		print(faker.uri())
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")

			
if command == "12":
	time.sleep(0.2)

	print(Fore.RESET + "\nРандомные числа от 0 до 9999999999\n")
	time.sleep(0.1)
	randomm = input("Сколько чисел хотите вывести: ")
	randomm = int(randomm) 
		
	for h in range(randomm):
		h = random.randint(0, 9999999999)
		print(h)
		time.sleep(0.2)

	
	input("\nНажмите Enter, чтобы выйти..")


if command == "8":
	print(Fore.RESET + "\nГенерация имён\n")

	name = input("Сколько имён хотите сгенерировать: ")
	name = int(name)
		
	for i in range(name):
		print(faker.name())
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")
		

if command == "5":
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
		time.sleep(0.2)
	
	input("\nНажмите Enter, чтобы выйти..")
	

if command == "11":
	time.sleep(0.2)
	
	numbers = random.randint(1, 10)
	print(numbers)

	input("\nНажмите Enter, чтобы выйти..")
	

if command == "10":
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
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")


if command == "4":
	time.sleep(0.3)
	print(Fore.RESET + "\nГенерация фамилии")
	
	fam = input("Количество фамилий: ")
	fam = int(fam)
	for f in range(fam):
		print(faker.last_name())
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")
		

if command == "13":
	time.sleep(0.2)
	print(Fore.RESET + "\nРандомайзер улиц\n")
	
	ul = input("Количество улиц: ")
	ul = int(ul)
	for h in range(ul):
		print(faker.street_address())
		time.sleep(0.2)

	input("\nНажмите Enter, чтобы выйти..")
		
	
if command == "14":
	print(Fore.RESET + "Выход из софта...")
