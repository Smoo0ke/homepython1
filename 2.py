#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.



x, y, z = map(int, input().split())

if not (x or y or z) == (not x and not y and not z):
    print("Утверждение не верно.")
else:
    print("Утверждение верно.")
