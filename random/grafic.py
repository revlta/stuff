import matplotlib.pyplot as plt
from matplotlib.ticker import *
# f = [180.7, 181.8, 182.7, 183.7, 185.0, 185.2, 185.4, 186.0, 186.3, 186.5, 186.6,
#      187.2, 188.3, 189.5, 190.1, 191.9, 192.0, 193.5, 194.9, 196.2, 197.5, 198.8]
# Unap = [11.0, 11.5, 12.5, 12.0, 18.5, 19.5, 18.0, 19.0, 17.5, 16.5,
#         18.0, 16.5, 15.0, 13.5, 13.0, 16.0, 18.0, 19.0, 13.0, 12.0, 11.5, 11.0]
# Uotn = [0.6, 0.6, 0.7, 0.9, 0.9, 1, 0.9, 0.9, 1, 0.9,
#         0.8, 0.8, 0.8, 0.9, 0.7, 0.7, 0.8, 1, 0.7, 0.6, 0.6, 0.6]
fig, ax = plt.subplots(figsize=(8, 6))
f = [180.7, 181.8, 182.7, 183.7, 185.2, 186.0, 187.2, 188.6, 189.5, 190.1]
Uotn = [0.6, 0.6, 0.6, 0.7, 1.0, 1.0, 0.8, 0.9, 0.7, 0.7]
plt.plot(f, Uotn)
plt.scatter(f, Uotn)
# plt.plot(f, Unap)
# plt.scatter(f, Unap)

plt.xlabel('частота')  # для оси x
plt.ylabel('напряжение')  # для оси y
plt.title('график')  # заголовок
plt.grid(which='major', linewidth=1)
plt.grid(which='minor', color='grey' ,linewidth=0.5)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.tick_params(which='major', length=10, width=2)
plt.tick_params(which='minor', length=5, width=1)
plt.show()  # посмотрим, что у нас получилось
