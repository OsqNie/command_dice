# DND roll die script, made to automate complicated rolls
# Oskar Niemenoja, Oct 2020

# USAGE:
# (x)dy 	- roll y-sided die x times. If x is left out, default 1
# a 	- roll with advantage (add one die and remove the lowest from the sum)
# d 	- roll with disadvantage (add one die, remove largest)
# ex	- add a modifier of x to each roll
# ox	- add a modifier of x once
# rx	- repeat for x identical throws
# 
# d20 a 	- Roll a d20 with advantage
# d20 e4 r2	- Roll 2 attack rolls, adding +4 modifier to each
# 6d6 o4	- Roll 6 six-sided dies, adding 4 to the total

from re import search
from random import randint
from sys import argv

def roll(string, verbose = True):
	# detect (x)dy
	roll = search(r'\b([0-9]*)d([0-9]+)\b', string)
	if roll == None:
		pass
	roll = list(roll.groups()) # Fetch the rolls
	if roll[0] == '':
		roll[0] = 1 # enables rolls without specifying dice, default 1
	adv = search(r'\ba\b', string) is not None # Advantage
	dis = search(r'\bd\b', string) is not None # Disadvantage

	if adv and dis: # Both cancel each other out
		adv = False
		dis = False

	repeat = search(r'\br([0-9]+)\b', string) # How many times to repeat
	add_to_each = search(r'\be([0-9]+)\b', string) # The modifier for each throw
	add_once = search(r'\bo([0-9]+)\b', string) # The modifier for total
	
	times, dice = map(int,roll) # Extract the throws and dice faces from the roll
	repeat = int(repeat.groups()[0]) if repeat is not None else 1 # Default repeats 1
	add_to_each = int(add_to_each.groups()[0]) if add_to_each is not None else 0 # Default modifier 0
	add_once = int(add_once.groups()[0]) if add_once is not None else 0 # Default modifier 0

	for i in range(repeat):
		tot_sum = 0
		
		# For adv / dis handling
		times_modified = times

		if adv:
			times_modified += 1
		if dis:
			times_modified += 1

		# Save the throws
		rolls = []
		for j in range(times_modified):
			rolls.append(randint(1,dice))

		# Discard min / max accordingly
		if adv:
			rem_adv = min(rolls)
			rolls.remove(min(rolls))
		if dis:
			rem_dis = max(rolls)
			rolls.remove(max(rolls))
		
		if verbose:
			# Create the string to display
			roll_str = 'Rolled {} (['.format(sum(rolls) + add_to_each * times + add_once)

			roll_str += ', '.join(str(roll) for roll in rolls)		
			roll_str += ']'
			if add_to_each != 0:
				if times == 1:
					roll_str += ' + {}'.format(add_to_each * times)
				else:
					roll_str += ' + {} ({} * {})'.format(add_to_each * times, add_to_each, times)
			if add_once != 0:
				roll_str += ' + {}'.format(add_once)
			
			if adv:
				roll_str += ', removed [{}] (advantage)'.format(rem_adv)
			if dis:
				roll_str += ', removed [{}] (disadvantage)'.format(rem_dis)

			roll_str += ')'

			print(roll_str)

		return sum(rolls) + add_to_each * times + add_once

# Default run: use the command line arguments as input
if __name__ == '__main__':
	roll(' '.join(argv[1:]))