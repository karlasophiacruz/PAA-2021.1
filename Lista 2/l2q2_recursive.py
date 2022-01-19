import matplotlib.pyplot as plt
import time

def fibonacci(n):                           
    if n <= 1:                              
        return n                             
    else:                                  
        return fibonacci(n - 1) + fibonacci(n - 2)

start_time = time.time()
plt.switch_backend('TkAgg')
plt.style.use('seaborn-whitegrid')
hfont = {'fontname':'Helvetica'}

x = []
y = []
n = 1

while((time.time() - start_time) <= 60):
  fibonacci(n)
  x.append(n)
  y.append(time.time() - start_time)
  n = n + 1

plt.plot(y, x, c = 'b', label = "Recursive")
plt.ylabel('Time (s)')
plt.xlabel('n')
plt.legend()
plt.title('Fibonacci Recursive Algorithm')
plt.show()