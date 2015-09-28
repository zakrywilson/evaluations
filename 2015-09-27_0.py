# Zach Wilson
# 09/27/2015

# Source: TopCoder, Name CatchTheBeastEasy

def able_to_catch_all(xs, ys):
   if sum(ys) >= max(abs(x) for x in xs):
      return "Good"
   return "Bad"

print '1: good -', able_to_catch_all([-1,1,0],[1,3,4])
print '2: bad -', able_to_catch_all([-3],[2])
print '3: good -', able_to_catch_all([0,-1,1],[9,1,3])
print '4: bad -', able_to_catch_all([70,-108,52,-70,84,-29,66,-33],[141,299,402,280,28,363,427,232])
print '5: good -', able_to_catch_all([-175,-28,-207,-29,-43,-183,-175,-112,-183,-31,-25,-66,-114,-116,-66],[320,107,379,72,126,445,318,255,445,62,52,184,247,245,185])
print '6: good -', able_to_catch_all([0,0,0,0],[0,0,0,0])
