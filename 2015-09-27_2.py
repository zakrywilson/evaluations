# Zach Wilson
# 09/27/2015

# Source: TopCoder, Name: AddMultiply

def make_expression(y):
   return [.5, 2, y - 1]

def test_it(x,y):
   if (x[0] * x[1]) + x[2] == y:
      return "true"
   return "false"

y = 6
x = make_expression(y)
print 'x: ', x
print 'passed? ', test_it(x,y)
