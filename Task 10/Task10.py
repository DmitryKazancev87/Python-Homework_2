# #Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
#которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.

n=int(input('Введите количество монеток (n) на столе:'))
SumOrel=0
SumReshka=0
for i in range(n):
    k=int(input('Введите стороны монеток которые лежат на столе : (где 0 - это Орел, а 1 - это Решка)'))
    if k==0:
        SumOrel+=1
    else:
         SumReshka+=1
if SumOrel<SumReshka:             
    print(f'Из {n} монет на столе необходимо минимально перевернуть {SumOrel} монеток с Орлом.')
else:
      print(f'Из {n} монет на столе необходимо минимально перевернуть {SumReshka} монеток с Решкой.')