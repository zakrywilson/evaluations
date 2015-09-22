# Zach Wilson
# 9/21/2015

# Source: TopCoder
# A sentence is called dancing if its first letter is uppercase and the case of each 
# subsequent letter is the opposite of the previous letter. Spaces should be ignored when 
# determining the case of a letter. For example, "A b Cd" is a dancing sentence because 
# the first letter ('A') is uppercase, the next letter ('b') is lowercase, the next letter 
# ('C') is uppercase, and the next letter ('d') is lowercase.

# test data
sentence_0 = 'This is a dancing sentence'
sentence_1 = ' This   is         a  dancing   sentence  '
sentence_2 = 'aaaaaaaaaaa'

class DancingSentence:

	@staticmethod
	def makeDancing(sentence):
		new_sentence = ''
		counter = 0
		for letter in sentence:
			if not letter == ' ':
				if (counter % 2) == 0: # even numbers
					new_sentence += letter.capitalize()
				else: # odd numbers
					new_sentence += letter.lower()
				counter += 1
			else:
				new_sentence += letter
		sentence = new_sentence
		return sentence

# test case
print DancingSentence.makeDancing(sentence_1)