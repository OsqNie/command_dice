# DND roll die script, made to automate complicated rolls
Oskar Niemenoja, Oct 2020

# USAGE:
```
parameters:
string  - the roll string
verbose - True / False, default True. Print the output (True) 

Return:
sum     - The roll sum

(x)dy 	- roll y-sided die x times. If x is left out, default 1
a 	- roll with advantage (add one die and remove the lowest from the sum)
d 	- roll with disadvantage (add one die, remove largest)
ex	- add a modifier of x to each roll
ox	- add a modifier of x once
rx	- repeat for x identical throws
 
d20 a 	- Roll a d20 with advantage
d20 e4 r2	- Roll 2 attack rolls, adding +4 modifier to each
6d6 o4	- Roll 6 six-sided dies, adding 4 to the total
```

You can either call the script from the command line 
```
python roll.py 2d20 e4
```
or import the library and use the roll-function.
