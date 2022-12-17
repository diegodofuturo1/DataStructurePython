import numpy

#Lista: Crie uma estrutura de repeti��o para fazer a leitura de 5 n�meros 
#inteiros e os armazene dentro de uma lista. Ap�s a leitura, crie outra 
#estrutura de repeti��o para somar todos os valores digitados

numbers = []

for i in range(5):
    numbers.append(int(input('Number: ')))

_sum = 0

for number in numbers:
    _sum += number

print(_sum)

#Dicion�rio: Crie um dicion�rio para armazenar o nome e a nota de 3 alunos,
#fazendo a leitura dos valores por meio de uma estrutura de repeti��o. 
#Depois, crie uma nova estrutura de repeti��o para somar todas as notas e
#retornar a m�dia

stundents = {
    'Ana': [10, 8, 9],
    'Bia': [1, 2, 5],
    'Cia': [5, 8, 7],    
}

for name, grades in stundents.items():
    _sum = 0
    for grade in grades:
        _sum += grade
    mean = _sum / len(grades)
    print(f'{name} tem media {round(mean, 1)}')

#Matriz: Dada a matriz abaixo, construa uma estrutura de repeti��o para 
#percorrer e somar todos os elementos da matriz

matrix = numpy.array([
    [3,4,1],
    [3,1,5]
])

_sum = 0

for row in matrix:
    for column in row:
        _sum += column

print(_sum)