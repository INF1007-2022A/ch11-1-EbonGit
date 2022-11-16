from game import *

def deal_damage(a,b):
	print(f"{b.name} used {b.weapon.name}")
	print(f'  {a.name} took {b.compute_damage(a)} dmg')

def run_battle(a,b):
	return None


def main():
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmor", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	deal_damage(c1, c2)




if __name__ == "__main__":
	main()

