
def message():
    print('Function created successful!')

message()

def message(text):
    print(text)

message('Function with parameters created successful!')

def sum(a, b):
    print(f'{a} + {b} = {a+b}')

sum(2, 4)


def sum(a, b):
    return a + b

print(f'2 + 4 = {sum(2, 4)}')

def calculateGravitationalPotentialEnergy(m, h, g = 10):
    return g * m * h

print(
    calculateGravitationalPotentialEnergy(30, 12),
    calculateGravitationalPotentialEnergy(30, 12, 9.8)
)