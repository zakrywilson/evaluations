# Zach Wilson
# 9/20/2015

# Given two unsorted lists of integers, for example: [ 1, 20, 4 ] 
# and [ 8, 2, 40 ], determine the common scale factor for each 
# element, assuming the elements were paired together correctly. In the
# example, after the elements have been paired correctly, we find that 
# 1 * 2 = 2, 20 * 2 = 40, and 4 * 2 = 8, meaning the common factor is 2.

a = [10, 4, 18, 6, 14]  # = 52 
b = [7,  3, 2,  9, 5]  # = 26

a_sum = 0.0
b_sum = 0.0

for a_index, b_index in zip(a, b):
   a_sum += a_index
   b_sum += b_index

print "factor sum: ", b_sum / a_sum
