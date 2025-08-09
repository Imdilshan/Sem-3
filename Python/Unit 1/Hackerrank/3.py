# Leap year

if (year % 400 == 0):
  leap = True;
elif (year % 4 == 0 and year % 100 != 0):
  leap = True;
else:
  leap = False;
