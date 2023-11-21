import matplotlib
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.1)

# Create the membership functions
mem_val = fuzz.trapmf(x, [1, 5, 7, 8])
# Plot the results of the linear fuzzy membership
plt.figure()
plt.plot(x, mem_val, 'b', linewidth=1.5, label='Membership Function')  # Added label
plt.ylabel('Membership degree')
plt.xlabel('Universe of Discourse')
plt.legend()  # Added this line to display the legend
plt.show()