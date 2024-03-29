4. резистор 2

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
