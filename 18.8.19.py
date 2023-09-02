num_tick = int(input("Количество билетов: "))
price = 0
age = [int(input("Возраст посетителя: ")) for i in range(num_tick)]
for i in range(len(age)):
    if age[i] < 18:
        price += 0
    elif 18 <= age[i] < 25:
        price += 990
    elif age[i] >= 25:
        price += 1390
print("Сумма покупки билетов без скидки: ", price)
if num_tick > 3:
    price = price * 0.9
print("Сумма покупки билетов со скидкой: ", price)