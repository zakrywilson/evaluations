# Zach Wilson
# 09/25/2015

# Source: TopCoder, Name: WritingWords

def write(word):
   count = 0
   for char in word:
      count += ord(char) - 64
   return count

print write("A") # returns 1
print write("ABC") # returns 6
print write("VAMOSGIMNASIA") # returns 143
print write("TOPCODER") # returns 96
