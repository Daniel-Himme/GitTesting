# import some useful modules
import matplotlib.pyplot as plt
import math

# initialise a list of length 10
x = [0] * 10
print(x)
# set the values in the list
for i in range(len(x)):
    x[i] = i
print(x)

y = [math.sin(i) for i in x]
print(y)
plt.plot(x, y, label='xy')
plt.legend()
plt.show()

# Your tasks:
# 1. add labels to x and y axes and plot title (search online or consult command line help)

# 2. change the colour of the line plot, add markers, add legend

# 3. add a second line plot of cos(x) and modify legend accordingly

# 4. from the pop-up window, save the plot with a name of your choosing in .png format

# 5. define a list named xx of length 100 with values in the range 0 to 2*math.pi. Plot xx vs. y. What happens? How can you fix it?

# 6. start a Python session in the terminal. type 'help()' and hit Enter. Read what it says and follow the instructions to quit the help utility.

# 7. type 'help(math)' and hit Enter. What happens?

# 8. Now type 'import math' and then 'help(math)'. Scroll down using Enter or down arrow key. Exit the math help menu by typing 'q'.

# Extra tasks:
# 9. Modify y so that if any of its entries are negative, they are changed to zero. Can you find more than one way to do it?

# 10. Find out how to save the plot without using the graphical interface in the popup window (i.e. do it with code).

# 11. Plot the two lines on two different sets of axes, but save them on the same image file.

# Created 2017 by jonathan.bull@it.uu.se and louis.j.van.rensburg@gmail.com
# Revised 2018 Ben Blamey ben.blamey@it.uu.se