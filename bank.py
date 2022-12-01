money = int(input('Введите сумму вклада '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
x = per_cent['ТКБ']
TKB = int(money * x / 100)

ТКБ = money * (per_cent.get('ТКБ')/100)
СКБ = money * (per_cent.get('СКБ')/100)
ВТБ = money * (per_cent.get('ВТБ')/100)
СБЕР = money * (per_cent.get('СБЕР')/100)
deposit = [round(ТКБ), round(СКБ), round(ВТБ), round(СБЕР)]
