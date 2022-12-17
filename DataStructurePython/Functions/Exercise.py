# Ler uma temperatura em graus Celsius e apresent�-la convertida em graus Fahrenheit. 
# A f�rmula de convers�o � F = (9 * C + 160) / 5, na qual F � a temperatura em Fahrenheit
# e C � a temperatura em graus Celsius
# - Fun��o para ler e retorna o valor da temperatura (n�o recebe par�metro)
# - Fun��o para fazer o c�lculo (recebe como par�metro a temperatura em graus Celsius)
# - Fun��o para mostrar o resultado, recebendo como par�metro o valor e fazendo a impress�o

def inputCelsius():
    return float(input("Celsius: "))

def celsiusToFahrenheit(celcius):
    return (9*celcius+160)/5

def outputFahrenheit(fahrenhreit):
    print(f"Fahreheit: {fahrenhreit}\n")

celcius = inputCelsius()
fahrenhreit = celsiusToFahrenheit(celcius)
outputFahrenheit(fahrenhreit)


# Efetuar o c�lculo da quantidade de litros de combust�vel gasto em uma viagem, utilizando 
# um autom�vel que faz 12 Km por litro. Para obter o c�lculo, o usu�rio deve fornecer o 
# tempo gasto na viagem e a velocidade m�dia durante ela. Desta forma, ser� poss�vel obter 
# a dist�ncia percorrida com a f�rmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da 
# dist�ncia, basta calcular a quantidade de litros de combust�vel utilizada na viagem, com 
# a f�rmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da 
# velocidade m�dia, tempo gasto na viagem, a dist�ncia percorrida e a quantidade de litros
# utilizada na viagem

# - Fun��o para ler os valores (n�o recebe par�metro e retorna os dois valores)
# - Fun��o para calcular a dist�ncia (recebe como par�metro o tempo e a velocidade e retorna a dist�ncia)
# - Fun��o para calcular a quantidade de litros (recebe como par�metro a dist�ncia e retorna os litros)
# - Fun��o para apresentar o resultado (recebe como par�metro os valores e somente imprime  o resultado)

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