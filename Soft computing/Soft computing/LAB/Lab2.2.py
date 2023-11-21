import matplotlib
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.arange(1, 10, 0.1)

# Create the membership functions
x_white = fuzz.gaussmf(x, 2, 3)
x_moderate = fuzz.gaussmf(x, 5, 3)
x_black = fuzz.gaussmf(x, 8, 3)
# Plot the results of the Gaussian fuzzy membership
plt.figure()
plt.plot(x, x_white, 'b', linewidth=1.5, label='white')
plt.plot(x, x_moderate, 'k', linewidth=1.5, label='moderate')
plt.plot(x, x_black, 'm', linewidth=1.5, label='black')
plt.title('Race of People, Gaussian Fuzzy')
plt.ylabel('Membership')
plt.xlabel('Race of People')
plt.legend(loc='center right', bbox_to_anchor=(1.5, 0.3),
           ncol=1, fancybox=True, shadow=True)
plt.show()