

import time as timer #https://docs.python.org/3/library/time.html

print(timer.time())

before = timer.time()
list = []

for i in range(0, 1000000):
    list.append(i)

after = timer.time()

print(before)
print(after)
print(after-before)

print("Python e uma linguagem Legen...")
timer.sleep(1)
print("Espera um pouquinho...")
timer.sleep(3)
print("(...) daria!")
