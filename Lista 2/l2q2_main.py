import matplotlib.pyplot as plt
import time

def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fibonacci2(n):                           
    if n <= 1:                              
        return n                             
    else:                                  
        return fibonacci2(n - 1) + fibonacci2(n - 2)

plt.switch_backend('TkAgg')
plt.style.use('seaborn-whitegrid')
hfont = {'fontname':'Helvetica'}

x = []
x2 = []
y = []
y2 = []
n = 1
n1 = 1

start_time = time.time()
while((time.time() - start_time) <= 60 and n <= 36):
  fibonacci(n)
  y.append(n)
  x.append((time.time() - start_time))
  n = n + 1

start_time = time.time()
while((time.time() - start_time) <= 60 and n1 <= 36):
  fibonacci2(n1)
  y2.append(n1)
  x2.append((time.time() - start_time))
  n1 = n1 + 1

plt.plot(y, x, c = 'r', label = "Iterative")
plt.plot(y2, x2, c = 'b', label = "Recursive")
plt.ylabel('Time (s)')
plt.xlabel('n')
plt.legend()
plt.title('Fibonacci Algorithm Comparative')
plt.show()