"""
Coin Flip Simulation - Write some code that simulates flipping a
single coin however many times the user decides. The code should
record the outcomes and count the number of tails and heads.
"""

import random


def coin_flip():
	coin = random.randint(0,1)
	if coin == 0:
		return "Head"
	if coin == 1:
		return "Tail"


def coin_outcomes():
	flip = "Y"
	results = []
	while flip == "Y":
		flip = input("Flip coin? Y/N ").upper()
		this_round = coin_flip()
		print("You got " + this_round)
		results.append(this_round)
		if flip != "Y":
			break
		else:
			continue
	heads = results.count("Head")
	tails = results.count("Tail")
	print(f"\nYou got {heads} Heads and {tails} Tails.")

if __name__ == '__main__':
	coin_outcomes()