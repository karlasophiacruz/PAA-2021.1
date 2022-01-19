import matplotlib.pyplot as plt
import time

def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

plt.switch_backend('TkAgg')
plt.style.use('seaborn-whitegrid')
hfont = {'fontname':'Helvetica'}

x = []
y = []
n = 1

start_time = time.time()
while((time.time() - start_time) <= 60):
  fibonacci(n)
  x.append(n)
  y.append((time.time() - start_time))
  n = n + 1

plt.plot(y, x, c = 'r', label = "Iterative")
plt.ylabel('Time (s)')
plt.xlabel('n')
plt.legend()
plt.title('Fibonacci Iterative Algorithm')
plt.show()