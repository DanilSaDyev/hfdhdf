2. Среднее арифметическое число

def middleAr(*args):
sum = 0
for i in args:
sum += i
return sum / len(args)


print(middleAr(1,4,5))
