# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
#
# ford = ford.upper()
# audi = audi.replace(" ","")
# citroen = citroen.upper().replace("-","")
#
# print(audi,citroen,ford,honda)

# shopping_list = []
#
#
# while True:
#     x = input("co chcesz dodac do listy ? ")
# shopping_list.append(x)
#
# print(shopping_list)

#zadania listy
#zadanie 1
#
# favourite_sports = [
#     "pilka nozna",
#     "plywanie",
#     "bieganie",
#     "wspinaczka",
#     "latanie",
#     "strzelectwo",
#     "silownia"
# ]
#
# favourite_sports[1] = "skakanie"
#
# print(favourite_sports)


#zadanie 2
#
# i = 0
# favourite_dishes = []
# for i in range(3):
#     x = input("Podaj ulubione potrwawy ")
#     favourite_dishes.append(x)
#
#
#
# print(favourite_dishes)
#
#
# phone_number = []
# i = 0
# for i in range(6):
#     x = int(input("podaj liczby numeru telefonu "))
#     phone_number.append(x)
#
# y = 0
#
# for y in range(3):
#     z = int(input("podaj liczby telefonu "))
#     phone_number.append(z)
#
# blocked_number = phone_number
#
# blocked_number[6:8] = "-"
#
# print(blocked_number)


#moja alternatywna wersja rozwiazania tego zadania
# phone_number = input("podaj numer telefonu ")
#
# public_number = phone_number[:6]
#
# blocked_number = phone_number[6:]
#
# blocked_number = 3 *  "-"
#
# print(public_number + blocked_number)
#
#
#
#
#Slowniki

# polish_to_english = {
#     "burza" : "storm",
#     "amnezja" : "amnesia",
#     "pilka": "ball",
# }

#
# #print(f"Z angielskiego pilka to {polish_to_english['pilka']}")
#
# #print(polish_to_english['amnezja'])
#
# teacher = {
#     "first_name" : "Bartek",
#     "second_name" : "Becela",
#     "date_of_birth" : "1997-09-15",
#     "wyksztalcenie" : {
#         "studia": "licencjat",
#         "liceum" : "tak",
#     }
#
#
# }
#
#
# teacher["first_name"] = "Karol"
#
# teacher["city"] = "Milicz"
# #metoda pop wyciaga nam cos ze slownika czyli jakby usuwa
#
# # second_name = teacher.pop("second_name")
#
# # print(teacher.keys())  #wypisuje klucze slownika
# # print(teacher.values())  #wypisuje wartosci slownika
#
# # keys = list(teacher.keys())   # zamiana wartosci klucza ze slownika na liste
# # print(keys)
# # values = list(teacher.values())   #zamiana wartosci slownika na liste
# # print(values)
#
#
# print(len(teacher))   # liczba elementow w slowniku

#zadanie 1 slowniki

# oceny = {
#     "matematyka" : "3,4,5,4,5,6",
#     "chemia" : "3,3,2,4,3,2,2",
#     "biologia": "3,4,5,6,5,4,3,5",
#     "polski": "3,4,2,1,2,3,2"
#
#
# }
#
# print(list(oceny.keys()))

#Zadanie 2


#zadanie 3

# expediture = {
#     "jedzenie ": int(input("ile wydajesz na jedzenie? ")),
#     "rozrywka" : int(input("ile wydajesz na rozrywke? ")),
#     "oplaty" : int(input("ile wydajesz na oplaty? ")),
#     "inne" : int(input("ile wydajesz na inne? "))
#
# }
#
# wydatki_jedzenie = expediture.get("jedzenie ")
# print(wydatki_jedzenie)
#
# values_lista_jedzenie = list(expediture.values())
# jedzenie = values_lista_jedzenie[0]
# rozrywka = values_lista_jedzenie[1]
# oplaty = values_lista_jedzenie[2]
# inne = values_lista_jedzenie[3]
# suma = jedzenie + rozrywka + oplaty + inne
#
# selected_category = input("wybierz kateogrie (jedzenie/rozrywka/oplaty/inne: ")
# print(f"udzial procentowy jedzenia to {(rozrywka/suma) * 100}, udzial procentowy rozrywki {(rozrywka/suma)*100} , procent oplat w calosci to {(oplaty/suma)*100}, procent innych wydatkow to {(inne/suma)*100} ")
#
#
#

# print(values_lista_jedzenie)

