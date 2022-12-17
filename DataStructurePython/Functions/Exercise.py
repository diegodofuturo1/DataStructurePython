# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit
# e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def inputCelsius():
    return float(input("Celsius: "))

def celsiusToFahrenheit(celcius):
    return (9*celcius+160)/5

def outputFahrenheit(fahrenhreit):
    print(f"Fahreheit: {fahrenhreit}\n")

celcius = inputCelsius()
fahrenhreit = celsiusToFahrenheit(celcius)
outputFahrenheit(fahrenhreit)


# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando 
# um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o 
# tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter 
# a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da 
# distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com 
# a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da 
# velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros
# utilizada na viagem

# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime  o resultado)

def inputTime():
    return float(input("Time (h): "))

def inputSpeed():
    return float(input("Speed (km\h): "))

def calculateDistance(time, speed):
    return time * speed

def calculateFuel(distance, kilometersPerLiter):
    return distance / kilometersPerLiter

def outputFuelSpentOnATrip(time, speed, distance, kilometersPerLiter, fuel):
    print(f"Time: {time} h\nSpeed: {speed} km\h\nDistance: {distance} km\nKilometers Per Liter: {kilometersPerLiter} km\l\nFuel Spent: {fuel} l\n")

kilometersPerLiter = 12
time = inputTime()
speed = inputSpeed()
distance = calculateDistance(time, speed)
fuel = calculateFuel(distance, kilometersPerLiter)
outputFuelSpentOnATrip(time, speed, distance, kilometersPerLiter, fuel)