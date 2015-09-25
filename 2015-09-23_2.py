# Zach Wilson
# 09/23/2015

# Source TopCoder
#
# Limak is an old brown bear. Because of his bad eyesight he sometimes has to visit his 
# doctor, Dr. Carrot. Today is one such day.
#
# Dr. Carrot has a blackboard in his office. There is a number A written on the 
# blackboard. In order to examine Limak's eyesight, Dr. Carrot asked him to read the 
# number. Limak couldn't see the number really well. He could determine the number of 
# digits correctly, but he was not sure what the individual digits are. Finally, he 
# decided to announce the number B to the doctor. The doctor then left the office for a 
# short while.
#
# Limak really doesn't want to wear glasses, so he has decided to cheat. As soon as the 
# doctor left the room, Limak went to the blackboard to read the correct number A. Before 
# the doctor returns, Limak has the time to change one of the digits of A to any different 
# digit. (Note that he may not add any new digits to A and he may not completely erase any 
# digits of A. He may only change at most one of the digits.) Limak hopes that he can 
# deceive the doctor by changing the number A into his number B.
#
# You are given the ints A and B. Return the String "happy" (quotes for clarity) if 
# Limak can convince the doctor that his eyesight is good. Otherwise, return the String 
# "glasses".

def eye_sight(A, B):

	different_digits = 0
	for a_digit, b_digit in zip(str(A), str(B)):
		different_digits += 1 if a_digit != b_digit else 0
	return 'happy' if different_digits < 2 else 'glasses'

# test cases
print eye_sight(8072, 3072) # happy
print eye_sight(508, 540) # glasses
print eye_sight(854000, 854000) # happy
print eye_sight(1, 6) # happy
print eye_sight(385900, 123000) # glasses






































