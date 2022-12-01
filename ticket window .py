ticket = int(input('Количство билетов: '))

sum = 0
for i in range(ticket):
    age = int(input('Возраст: '))
if age <18:
    sum += sum
elif 18 <= sum < 25:
    sum += 990
else:
    sum = 1390
print(sum)

if ticket > 3:
    sum = sum * 0.9
print(sum)
