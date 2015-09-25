# Zach Wilson
# 09/24/2015
#
##########################################################################################
# Source: TopCoder
# Name: Problem Statement for TwoWaysSorting
#
# Sasha has a String[] stringList. No two elements of stringList have the same length.
#
# So far, Sasha has learned two ways of sorting strings:
#
# He can sort strings lexicographically. For example, "car" < "carriage" < "cats" < 
# "doggies". (See Notes for a definition of the lexicographic order.)
# He can also sort strings according to their lengths in ascending order. For example, 
# "car" < "cats" < "doggies" < "carriage".
#
# Sasha now wonders whether stringList is sorted in either of these two ways. Return 
# "lexicographically" (quotes for clarity) if stringList is sorted lexicographically but 
# not according to the string lengths. Return "lengths" if stringList is sorted according 
# to the string lengths but not lexicographically. Return "both" if it is sorted in both 
# ways. Otherwise, return "none".
##########################################################################################


def sorting_method(string_list):

	current = None
	next = None

	lex = True
	length = True

	for index, obj in enumerate(string_list):
		
		if index != len(string_list) - 1:
			
			next = string_list[index + 1]
			current = string_list[index]

			tally =  01 if (current < next) else 00					# test for lex
			tally += 10 if (len(current) < len(next)) else 00		# test for length

			if tally == 00:		# if "none"...
				return "none"
			elif tally == 01:		# if not "lengths"...
				length = False
			elif tally == 10:		# if not "lexicographically"...
				lex = False

		else:
			if (length == True) and (lex == True):
				return "both"
			else:
				return "lexicographicall" if lex == True else "lengths"


##########################################################################################
# test cases:
print sorting_method(['a', 'aa', 'bbb'])  # returns "both"
print sorting_method(['c', 'bb', 'aaa'])  # returns "lengths"
print sorting_method(['etdfgfh', 'aio'])  # returns "none"
print sorting_method(['aaa', 'z']) 			# returns "lexicographically"
print sorting_method(['z'])					# returns "both"
print sorting_method(['abcdef', 'bcdef', 'cdef', 'def', 'ef', 'f', 'topcoder']) 
														# returns "lexioographically"