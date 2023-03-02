# p1 = input('Введите пароль')
# p2 = input('Повторите пароль')
# if p1 == p2 and p1 != 'qwerty':
#     print('Принято')
# elif p1 == 'qwerty' or len(p1)<8:
#     print('Пароль ненадежный')
# elif p1 != p2:
#     print('Пароли не совпадают')
m=int(input('Введите ваше место'))
if m <= 36:
    if m % 2 == 0:
        print('Верхнее')
    else:
        print('Нижнее')
elif m>36 and m <= 54:
    if m % 2 == 0:
        print('Верхнее боковое')
    else:
        print('Нижнее боковое')
else:
    print('Такого места не существует')
# y=int(input('Введите год'))
# if y%4==0 and y%100!= 0 or y%400==0:
#     print('Год високосный')
# else:
#     print('Год невисокосный')

# c1, c2 = input('Введите 1 цвет'), input('Введите 2 цвет')
# if c1 == 'красный' and c2 == 'синий' or c2 == 'красный' and c1 == 'синий':
#     print('фиолетовый')
# if c1 == 'красный' and c2 == 'жёлтый' or c2 == 'красный' and c1 == 'жёлтый':
#     print('оранжевый')
# if c1 == 'жёлтый' and c2 == 'синий' or c2 == 'жёлтый' and c1 == 'синий':
#     print('зелёный')

# n=int(input('Введите N'))
# res=''
# for i in range(n):
#     s=input()
#     res= res+s+ ' '
# print(res)