import numpy as np
import matplotlib.pyplot as plt

def gaussian_membership(x, mean, std_dev):
    return np.exp(-0.5 * ((x - mean) / std_dev)**2)

# Temperature values for the x-axis
x = np.arange(-10, 40, 0.1)

# Membership functions parameters (mean and standard deviation)
warm_mean, warm_std_dev = 25, 5
moderate_mean, moderate_std_dev = 15, 5
cold_mean, cold_std_dev = 5, 5
hot_mean, hot_std_dev = 35, 5

# Calculate membership degrees for each linguistic term
warm_membership = gaussian_membership(x, warm_mean, warm_std_dev)
moderate_membership = gaussian_membership(x, moderate_mean, moderate_std_dev)
cold_membership = gaussian_membership(x, cold_mean, cold_std_dev)
hot_membership = gaussian_membership(x, hot_mean, hot_std_dev)

# Plot the membership functions
plt.figure(figsize=(10, 6))
plt.plot(x, warm_membership, 'r', label='Warm')
plt.plot(x, moderate_membership, 'g', label='Moderate')
plt.plot(x, cold_membership, 'b', label='Cold')
plt.plot(x, hot_membership, 'm', label='Hot')

plt.title('Temperature Fuzzy Membership Functions')
plt.xlabel('Temperature')
plt.ylabel('Membership')
plt.legend()
plt.grid()

plt.show()
