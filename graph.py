import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
y = np.arange(2,11,2)

fig = plt.figure()

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.2,0.3])

#axes1-------
axes1.plot(y,x,"red")

axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outer Graph")

#axes2-------
axes2.plot(x,y,"red")

axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")



plt.show()