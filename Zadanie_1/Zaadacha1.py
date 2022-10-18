# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

numer = 0.56
st_numer = str(numer)
st_numer = st_numer.replace('.','')
lst_numer = list(st_numer)
lst_numer_n = map(int, lst_numer)
summa = sum(lst_numer_n)
print(summa)
