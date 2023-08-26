per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))
deposit = []
for count in per_cent.keys():
    deposit.append(int(per_cent[count] * money/100))
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))