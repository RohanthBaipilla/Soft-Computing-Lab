import mport as mport

import math
def fuzzify(x, mean, sigma):
 return 1 / (math.sqrt(2 * math.pi) * sigma) * math.exp(-(x - mean)**2 / (2 * sigma**2))
def defuzzify_cog(x, mean, sigma):
 area = 1 / (math.sqrt(2 * math.pi) * sigma) * math.exp(-(x - mean)**2 / (2 * sigma**2))
 return mean * area
if __name__ == "__main__":
 x = 3
 mean = 2
 sigma = 1
 print("Fuzzified value:", fuzzify(x, mean, sigma))
 print("Defuzzified value (COG):", defuzzify_cog(x, mean, sigma))