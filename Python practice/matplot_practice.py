import numpy as np
import matplotlib.pyplot as plt
#compute x and y
x=np.arange(0,3*np.pi,.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title("sine & cosine graph")
plt.legend(['Sine','Cosine'])
plt.show()

#trying for subplots

#1st plot no of plots in height required 2 and no of plots in width required 1
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title("sine")
#plt.legend(['sine'])
#2nd plot
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cosine')
#plt.legend(['cosine'])
plt.show()


