# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
#не превосходящие числа N.

num=2
N=int(input(f'Введите число (N) до которого необходимо вывести все целые степени числа {num}:'))
i=0
while num**i<=N: 
    print(f'цифра 2 в степени {i} равна - {num**i}.')
    i+=1
 
    