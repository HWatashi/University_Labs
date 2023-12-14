import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 5, 1000)  

y = 10 * np.cos(x**2) / x**2

plt.figure(figsize=(8, 6))  

plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r'$Y(x) = \frac{10 \cdot \cos(x^2)}{x^2}$')  # Графік функції

plt.axhline(0, color='black',linewidth=0.5)  
plt.axvline(0, color='black',linewidth=0.5) 

plt.xlabel('x')  
plt.ylabel('Y(x)')  
plt.title('Графік функції Y(x) = 10 * cos(x^2) / x^2')  

plt.legend()  

plt.grid(True)  

plt.show() 
