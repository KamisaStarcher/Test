#Kamden Starcher
#1-3-19
import random
import sys

class P:
	def __init__(self, clas, n):
		self.n = n
		self.clas = clas
		self.inv = []

		if clas == "Knight":
			self.max_hp = 10
			self.hp = self.max_hp
			self.dpi = 5
			self.range = 3
			self.move = 3

		if clas == "Archer":
			self.max_hp = 7
			self.hp = self.max_hp
			self.dpi = 7
			self.range = 6
			self.move = 6 

		if clas == "Mage":
			self.max_hp = 5
			self.hp = self.max_hp
			self.dpi = 0
			self.range = 10
			self.move = 4

class E:
	def __init__(self, health, pos, speed, dpi):
		self.hp = health
		self.pos = pos
		self.speed = speed
		self.dpi = dpi

class SB:
	def __init__(self, tpe):
		self.tpe = tpe

	def Use():
		if self.tpe == "Fire":
			self.sd = 2

		if self.tpe == "Ice":
			self.sd = 1

		if self.tpe == "Wind":
			self.sd = 1

	def Gust():
		if Target != False:
			Target.pos -= 3
			Target.hp-=self.sd
			print(Target.hp)
			print(Target.pos)

	def Lose_turn():
		if Target != False:
			Target.speed = 0
			Target.hp-=self.sd
			print(Target.hp)
			print(Target.speed)

	def Fire_bolt(self):
		if Target != False:
			Target.hp-=self.sd
			print(Target.hp)
			
def Charcter():
	Target = False
	print("Hello young adeventure")
	print("What is your name?")
	n = input(">>>")
	print("What is your profession")
	print("1. Knight")
	print("2. Archer")
	print("3. Mage")
	choice = input(">>>")

	if choice == "1":
		player = P("Knight", n)
		print("Health", player.hp)
		print("Damage", player.dpi)
		print("Range", player.range)
		print("Movement", player.move)

	elif choice == "2":
		player = P("Archer", n)
		print("Health", player.hp)
		print("Damage", player.dpi)
		print("Range", player.range)
		print("Movement", player.move)

	elif choice == "3":
		player = P("Mage", n)
		print("Health", player.hp)
		print("Damage", player.dpi)
		print("Range", player.range)
		print("Movement", player.move)
	
	else:
		print("System Error 101")
		Charcter()

	Gift(player.clas, player.inv, player.n)

def Gift(pc, pi, pn):
	if pc == "Knight":
		print("So you need a sword")
		print("-------------------")
		print("    Sword added    ")
		pi.append('sword')
		Encounter(pc, pn, pi)

	if pc == "Archer":
		print("A bow but no arrows")
		print("-------------------")
		print("  24 arrows added  ")
		player_arrow = 24
		pi.append(player_arrow)
		Encounter(pc, pn, pi)

	if pc == "Mage":
		BookOfFire = SB('Fire')
		print("A spellbook for the mage")
		print("------------------------")
		print("   Book a fire added    ")
		pi.append(BookOfFire)
		Encounter(pc, pn, pi)
		
def Encounter(pc, pn, piv):
	global player
	Target = E(10, 5, 4, 2)

	print("As you walk there is a goblin")
	print("walking in the under brush. ")
	print("")
	print("1. Attack")
	print("2. Sneak")
	print("3. Talk")
	choice = input(">>>")

	if choice == "1":
		Attack(pc, pn, piv)

	if choice == "2":
		Sneak(pn)

	if choice == "3":
		Talk(pn)

def Attack(pi,pn, piv):
	if pi == "Knight":
		print("You walk up to the goblin")
		print("Pull out your sword and stab")
		print("It in the back as it screams")
		print("")
		print("1. Loot")
		print("2. Continue")
		choice = input(">>>")

		if choice == "1":
			Loot(pn, piv)

		if choice == "2":
			End_game(pn)

	if pi == "Archer":
		print("You pull out your bow and knock")
		print("an arrow. You pull the string")
		print("back to your cheek and realese.")
		print("The arrow flies through the air")
		print("right into the back of the goblin.")
		print("")
		print("1. Loot")
		print("2. Continue")
		choice = input(">>>")

		if choice == "1":
			Loot(pn, piv)

		if choice == "2":
			End_game(pn)

	if pi == "Mage":
		print("You take the book of fire out")
		print("of your bag and read a spell")
		print("from it. A fire ball builds up")
		print("power right in front of your")
		print("chest. As you finish the spell")
		print("the fire ball shoots forward into")
		print("the back of the goblin and it as")
		print("the fire burns the goblin it turns")
		print("into a pile of ash. You put away the")
		print("book. It feels slightly heavier.")
		print("")
		print("1. Loot")
		print("2. Continue")
		choice = input(">>>")

		if choice == "1":
			Loot_M(pn, piv)

		if choice == "2":
			End_game()

def Sneak(pn):
	print("You crouch down and start")
	print("To slowly move past him.")
	End_game(pn)

def Talk(pn):
	print("You walk up to him and say")
	print("1. Hello there")
	print("2. May I help you")
	choice = input(">>>")

	if choice == "1":
		print('"Good very good" says the goblin.')
		print("He turns around and jumps on you.")
		End_game(pn)

	if choice == "2":
		print('"Yes I am hungry" says the goblin.')
		print("He turns around and jumps on you.")
		End_game(pn)

def Loot(pn, piv):
	lot = ["Fine Bow", "Sword", "BookOfIce"]
	loot = random.choice(lot)
	print("You find", loot, "on the goblin")
	piv.append(loot)
	End_game(pn)

def Loot_M(pn, piv):
	print("You find nothing in the")
	print("pile of ash left by the fire")
	End_game(pn)

def End_game(pn):
	print("Thanks for play testing", pn)
	print("Hope you enjoyed")
	sys.exit()

Charcter()