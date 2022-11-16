"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	def __init__(self,name,power,min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	UNARMED_POWER = 20

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""



class Character:

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self):
	    return self.__name

	def compute_damage(self,other):
		proba = random.randint(0,15)
		crit = 1
		if proba == 15:
			crit = 2
		rand = random.uniform(0.85,1)

		return (((((2*self.level)/5)+2) * self.weapon.power * (self.attack/other.defense)) / 50 + 2) * crit * rand

	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass

