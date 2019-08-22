# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    m = int('1' + '0' * ndigits)
    q = number * m
    c = int(q)
    i = int((q - c) * 10)
    if i >= 5:
        c += 1
    return c / m

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    result = []
    while ticket_number > 0:
        result.append(ticket_number % 10)
        ticket_number //= 10

    result.reverse()
    if result[0] + result[1] == result[-1] + result[-2]:
        num = 0
        for i, v in enumerate(reversed(result)):
            num += v * 10 ** i
        return num


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))