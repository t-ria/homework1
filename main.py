Name = "Vika"
print(Name)
Age = 19
print(Age)
print(Name * 5)
A = input("Сколько вам лет?")
print(A)

Q = input("Как вас зовут? ")
print(Q)

print("Привет", Q)
print("Говорят, что мудрость приходит С возрастом, но у тебя пришёл только возраст")
int_A = int(A)
print(int_A)
if int_A < 18:
    print("Что ты здесь делаешь? Иди обратно в школу...")
elif int_A > 18:
    print("А ты просто уходи")
print(Name[1::1])
print(Name[::-1])
print(Name[-3])
print(5)
len(Name)

p = int_A
suma = 0
nesuma = 1
while p > 0:
    digit = p % 10
    suma = suma + digit
    nesuma = nesuma * digit
    p = p // 10
print("Сумма", suma)
print("Произведение", nesuma)
B = A.lower()
B1 = A.swapcase()
B2 = A.title()
B3 = A.upper()

proverkaA = A.isalpha()
if proverkaA != True:
    print("Некорректный ввод")
j=0
jage=int(Age)
if jage > 150:
    j=j+1
if jage < 0:
    j=j+1
if j!=0:
    print("Неверно введён возраст")




