# Zach Wilson
# 09/23/2015

# Source: TopCoder
#
# Chandan loves to play with strings. He just learned a new operation: inserting one 
# string X into another string Y.
#
# When inserting X into Y, it is also allowed to place X at the beginning or at the end of 
# Y. For example, there are exactly five ways how to insert the string "ab" into the 
# string "????": you can produce one of the strings "ab????", "?ab???", "??ab??", 
# "???ab?", and "????ab".
#
# According to Chandan, a good string is a string that can be constructed in the following 
# way: Initially, he takes the empty string "". Then, he performs a sequence of zero or 
# more steps. In each step he inserts the string "ab" anywhere into the current string.
#
# According to the above definition, the strings "ab", "aabb", and "aababb" are good while 
# the strings "aab", "ba", and "abbb" are not good.
#
# Chandan's friend Ravi came up with a String s. Ravi asked Chandan whether it is a good 
# string. Return "Good" (quotes for clarity) if the string is good, or "Bad" if the string # is not good.

class GoodString:
	
	def isGood(self, s):
		
		a_count = 0
		answer = 'Good'
		for char in s:
			a_count += 1 if char == 'a' else -1
			if a_count < 0:
				answer = 'Bad'
				break 

		if not a_count == 0:
			answer = 'Bad'

		return answer

# test cases:
s0 = 'abababb'
s1 = 'ab'
s2 = 'ba'
s3 = 'aababb'
s4 = 'ababababababab'
s5 = 'aaaaaa'
s6 = 'aabbba'

good_string = GoodString()
print good_string.isGood(s0)