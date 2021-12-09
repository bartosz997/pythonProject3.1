# input_value = int(input("podaj ile chcesz dac na lokate?"))
#
# percent = int(input("na ile procent lokata"))
#
# time = int(input("na ile lat "))
#
# end_value = input_value * (1 + percent/100) ** time
# #1 sposób
# if end_value > 1.1 * input_value:
#    print("brawo zarobiles ponad 10% w tym czasie ")
#
# # 2 sposob
# print(f"({end_value>input_value * 1.1} zarobiles ponad 10 %")
# print(end_value)


# marks = {
#
#     "chemia" : "1,2,3,4,3,2",
#     "matematyka": "1,1,1,2,3,2,3",
#     "fizyka": "1,2,2,3,4,5,5",
#     "polski":"1,2,3,2,2,2,2,1",
#
# }
#
#
#
#
# lista = list(marks.values())[0]
#
# if "1" in lista:
#     print("nie zdales ")
#

#zadanie 4


#
# x = str(input("jak masz na imie ?"))
#
# name = list(x)
#
# if "a" in name[-1]:
#     print("jestes kobieta")
# else:
#     print("nie jestes kobieta ")

#
#
# x = int(input("ile zarabiasz miesiecznie ? "))
#
# y = int(input("ilu pracownikow zatrudniaz ? "))
#
# if x <= 15000 or y >= 3:
#     print("mozesz otrzymac dotacje")
# else:
#     print("nie mozesz otrzymac dotacji")
#
# choice = input(f"jaki jest wtoj wybror " "k/l")
# if choice == "l":
#     print("wybrales lokate")
#     input_value = int(input("podaj ile chcesz dac na lokate?"))
#
#     percent = int(input("na ile procent lokata"))
#
#     time = int(input("na ile lat "))
#
#     end_value = input_value * (1 + percent/100) ** time
#     #1 sposób
#     if end_value > 1.1 * input_value:
#        print("brawo zarobiles ponad 10% w tym czasie ")
#        print(end_value)
#     # # 2 sposob
#     # print(f"({end_value>input_value * 1.1} zarobiles ponad 10 %")
#     # print(end_value)
#
# elif choice == "k":
#     print("wybrales zdolnosc kredytowa")
#     credit = int(input("ile chcesz pozyczyc "))
#     income = int(input("ile miesiecznie zarabiasz"))
#     expediture = int(input("ile miesiecznie wydajesz "))
#     age = int(input("ile masz lat"))
#     wklad_wlasny = int(input("ile masz wladu wlasnego "))
#     lata_kredytu = int(input("na ile lat chcesz kredyt"))
#     percent = int(input(" na ile procent chcesz kredyt "))
#     dochod = income - expediture
#
#     rata = (credit * percent/100 ) / 12 + credit / (lata_kredytu * 12)
#
#     if age < 18 and wklad_wlasny < credit * 0.1:
#         print("nie mozesz wziac kredytu")
#     elif age > 18 and  0.1 * credit <= wklad_wlasny <= 0.2 * credit and dochod > rata + 2000:
#         print(f"mozesz wziac kredyt, Twoja rata to  {rata}")
#     elif age > 18 and wklad_wlasny  > 0.2 * credit and dochod > rata + 1000:
#         print(f"mozesz wziac kredyt Twoja rata to {rata}")
#     # elif age > 18 and wklad_wlasny * 0.2 < credit < wklad_wlasny * 1:
#     #     print("mozesz brac kredyt")



# sex = input("jestes kobieta czy mezczyzna ? k/m")
# age = int(input(" ile masz lat"))
# score = float(input("jaki miales wynik w metrach ?"))
# if sex == "k":
#     if age == 13 and score > 2000:
#       print("bardzo dobry wybnik")
#     elif  2000>score>1500:
#        print("tak srednio")
#     elif 1000 < score < 1500:
#       print("bardzo slabo")
#     else:
#         print("fatalnie")
# if sex == "k":
#     if age == 13 and score > 2000:
#       print("bardzo dobry wybnik")
#     elif  2000>score>1500:
#        print("tak srednio")
#     elif 1000 < score < 1500:
#       print("bardzo slabo")
#     else:
#         print("fatalnie")


# #zadanie 2 operatory in oraz is zadanie
#
# phone_number = input("podaj numer telefonu")
# if "0" in phone_number:
#     print("zero jest w twoim numerze ")
#

#zadanie 1


#
# shopping_list = []
#
#
# x = input("podaj rzecz do listy zakupów")
#
# shopping_list.append(x)
#
# print(shopping_list)
# if 'bulka' or 'chleb' in shopping_list:
#     print("jest na liscie")



#dzial pętle

##zadanie 1

# i = 0
#
# while i < 10:
#     number =  int(input("podaj liczbe parzysta"))
#     if number % 2 ==0:
#         print("ss")
#         i +=1
#     else:
#         print("miala byc parzysta!")
#

#zadanie 2


# i = 0
#
# number = input("podaj numer telefonu")
# number = number.replace(",","").replace("-","")
# formated_number = ""
# while i < len(number):
#     if i % 3 ==0 and i !=0:
#         formated_number +="-"
#     formated_number += number[i]
#     i +=1
# print(formated_number)


#
# danie1 = input("podaj swoje ulubione dania rozdzielone przecinkiem")
# danie = danie1.split(",")
# i = 0
# while i <len(danie):
#
#     print(f"ulubione danie numer {i}: {danie[i]}")
#     i+=1



# kod_pocztowy = input("podaj kod pocztowy")
#
# i = 0
# kod_pocztowy.replace("-","").replace(" ","")
# formatowany = ""
# for i,cyfry in enumerate(kod_pocztowy):
#     if i % 2 ==0 and i !=0:
#         formatowany +="-"
#     formatowany +=cyfry
# print(formatowany)
#





# oceny = []
# ocena_input = input("podaj ocene albo zakoncz wciskajac X")
# while ocena_input != 'X':
#     ocena = int(ocena_input)
#     oceny.append(ocena)
#     ocena_input = input("podaj kolejna liczbe lub zakoncz X")
#
#
#
# suma_ocen = 0
# for ocena in oceny:
#     suma_ocen +=ocena
#
#
# srednia = suma_ocen/len(oceny)
# print(f"srednia to {srednia}")

# #Exercise 1: Print First 10 natural numbers using while loop
# x = 0
# while x <11:
#     print(x)
#     x +=1


# #Exercise 3: Calculate the sum of all numbers from 1 to a given number
#
# x = int(input("podaj liczbe calkowita"))
# suma = 0
# for i in range(x+1):
#     suma +=i
# print(suma)


# num = int(input("podaj liczbe parzysta"))
# suma = 0
# for i in range(num,20):
#     if i %2 ==0:
#         suma +=i
#     print(suma)


#
# # wypisze co 3 liczbe
# for number in range(1,13,3):
#     print(number)




# phone_number = input("podaj numer telefonu")
#
# phone_number = phone_number.replace(",","").replace(" ","")
#
# for digit in range(10):
#     digit_time_in_number = phone_number.count(str(digit))
#     print(f"cyfra {digit} wystepuje {digit_time_in_number}")
#

# lista = []
#
# x = input("podaj liszby ")
#
# for liczba in lista:
#     if liczba % 2 == 0:
#         print(liczba)
#     continue
# def put_a_brick():
#     print("-",sep="",end="")
#
#
#
# def build_a_wall(wall_lenght):
#     for brick in range(wall_lenght):
#         put_a_brick()
#     print()
#

# def prostokat(a,b):
#     return print(a*b)
#
#
# prostokat(10,2)
#
# def srednia(dystans,czas):
#     return print(f"{dystans/czas} km/h to srednia predkosc  ")
#
# wybor= input("jezeli chcesz policzyc srednia predkosc jazdy  samochodem wybierz S , jezeli chcesz policzyc predkosc na rowerze wybierz R jezeli biegu wybierz B")
# x = int(input("podaj dystan przejechany samochodem "))
# y = int(input("podaj czas jazdy samochodem"))
# if wybor == "S":
#     print((f"{srednia(x,y)} sredni czas jazdy samochodem"))
# elif wybor == "R":
#     print((f"{srednia(x,y)} sredni czas jazdy rowerem"))
# elif wybor == "B":
#     print((f"{srednia(x,y)} sredni czas biegu "))

# from math import *
#
# def pitagoras(a,b):
#     c = sqrt(a ** 2 + b ** 2)
#     print(c)
#
#
# pitagoras(3,4)





