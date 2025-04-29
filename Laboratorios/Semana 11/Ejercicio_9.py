import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]
plt.plot(x,y1,label="Serie 1",color="blue")
plt.plot(x,y2,label="Serie 2",color="green")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.legend()
plt.show()