# import matplotlib.pyplot as plt
# import numpy as np 

# #plot1 
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# plt.subplot(1,2,1)
# plt.plot(x,y)

# #plot2 
# x = np.array([1,1,2,3])
# y = np.array([10,20,30,40])
# plt.subplot(1,2,2)
# plt.plot(x,y)

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np 

# #plot1 
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# plt.subplot(2,1,1)
# plt.plot(x,y)

# #plot2 
# x = np.array([1,1,2,3])
# y = np.array([10,20,30,40])
# plt.subplot(2,1,2)
# plt.plot(x,y)

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np 

# #plot1 
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])
# plt.subplot(2,3,1)
# plt.plot(x,y)

# #plot2 
# x = np.array([1,1,2,3])
# y = np.array([10,20,30,40])
# plt.subplot(2,3,2)
# plt.plot(x,y)

# #plot3
# x = np.array([1,1,2,9])
# y = np.array([10,20,30,40])
# plt.subplot(2,3,3)
# plt.plot(x,y)

# #plot4
# x = np.array([0,1,2,3])
# y = np.array([10,20,30,40])
# plt.subplot(2,3,4)
# plt.plot(x,y)

# #plot5
# x = np.array([8,9,6,4])
# y = np.array([10,20,30,40])
# plt.subplot(2,3,5)
# plt.plot(x,y)

# #plot6
# x = np.array([1,8,2,7])
# y = np.array([10,20,30,40])
# plt.subplot(2,3,6)
# plt.plot(x,y)

# plt.show()


import matplotlib.pyplot as plt
import numpy as np 

#plot1 
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("Sales Team")

#plot2 
x = np.array([1,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.plot(x,y)
plt.title("Marketing Team")

#plot3
x = np.array([1,1,2,9])
y = np.array([10,20,30,40])
plt.subplot(2,3,3)
plt.plot(x,y)
plt.title("Finance Team")

#plot4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title("HR Team")

#plot5
x = np.array([8,9,6,4])
y = np.array([10,20,30,40])
plt.subplot(2,3,5)
plt.plot(x,y)
plt.title("IT Team")    

#plot6
x = np.array([1,8,2,7])
y = np.array([10,20,30,40])
plt.subplot(2,3,6)
plt.plot(x,y)
plt.title("Admin Team")

plt.suptitle("Company Performance")
plt.show()























