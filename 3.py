3. резистор
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
