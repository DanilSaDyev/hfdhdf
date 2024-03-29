1) Сумма от 1 до n
def cum(n):
sum = 0
for i in range(1, n + 1):
sum += i
return sum
#print(cum(5))
2. Среднее арифметическое число

def middleAr(*args):
sum = 0
for i in args:
sum += i
return sum / len(args)


print(middleAr(1,4,5))
3. ReSIStoooor
def resistor():
n = 10
i = 0
f1 = 0
f2 = 1
fsum = 0

while i < n:
print(fsum)
fsum = f1 + f2
f1 = f2
f2 = fsum
i = i + 1

resistor()

4. ReSIStoooor2

def resistor2():
i = 0
n = 5
r1 = 1
r2 = 1
curA = 0
pastA = 2 * r1 + r2

while i < n - 1:
curA = 2 * r1 + ((pastA * r2) / (pastA + r2))
pastA = curA
i += 1

return curA

print(resistor2())
