import numpy as np
import matplotlib.pyplot as plt

# Fuzzification using triangular membership functions
def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)

# Defuzzification using the centroid method
def defuzzify_centroid(membership_degrees, values):
    weighted_sum = 0
    total_area = 0

    for i in range(len(membership_degrees)):
        weighted_sum += membership_degrees[i] * values[i]
        total_area += membership_degrees[i]

    return weighted_sum / total_area if total_area != 0 else 0

# Temperature values for fuzzification
temperature = 25

# Membership function parameters
cold_membership = triangular_membership(temperature, 10, 15, 20)
moderate_membership = triangular_membership(temperature, 15, 20, 25)
hot_membership = triangular_membership(temperature, 20, 25, 30)

# Defuzzification
membership_degrees = [cold_membership, moderate_membership, hot_membership]
linguistic_terms = ['Cold', 'Moderate', 'Hot']
centroid_value = defuzzify_centroid(membership_degrees, [10, 20, 30])

# Print results
print("Membership degrees:", membership_degrees)
print("Linguistic terms:", linguistic_terms)
print("Defuzzified centroid value:", centroid_value)
