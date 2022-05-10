import random

"""
Blackjack Game Program
----------------------
Author: Manuel Sebastian Hernandez
Date Began: March 13th, 2022
Date (Single Player) Finished: April 17th, 2022
Date (Multiplayer) Finished: April 20th, 2022

alpha version 1.9
""" 

"""
	Main Program 
	------------
""" 

def main():		# main start

	"""
		Program Classes 
		---------------
	""" 

	class card():
		# Spades, Hearts, Diamonds, Clubs

		def __init__(self, suit, rank):
			self.__suit = suit
			self.__rank = rank
			self.__color = ''

		def __str__(self):
			return f"{self.__rank} of {self.__suit} ({self.__color})"

		def getSuit(self):
			return self.__suit

		def setSuit(self, suit):
			self.__suit = suit

		def getRank(self):
			return self.__rank

		def setRank(self, rank):
			self.__rank = rank

		def determineColor(self):
			if self.__suit == 'Spades' or self.__suit == 'Clubs':
				self.__color = 'Black'
			else:
				self.__color = 'Red'


	class dealer():

		def __init__(self): 
			self.__handTotal = 0

		def __str__(self):
			return f"Dealer's Hand Value: {self.__handTotal}"

		def getHandTotal(self):
			return self.__handTotal

		def addToHandTotal(self, num):
			self.__handTotal += num

		def resetHandTotal(self):
			self.__handTotal = 0


	class player():
		
		def __init__(self, playNum): 
			self.__cash = 0
			self.__bet = 0
			self.__playerNumber = playNum
			self.__handTotal = 0
			self.__splitHandTotal = 0
			self.playerHand = []
			self.hasBlackjack = False
			self.canPlay = True
			self.sitOut = False
			self.playerKicked = False
			playNum+=1

		def __str__(self):
			return f"\nPlayer {self.__playerNumber} has ${self.__cash}"

		def getPlayerHand(self):
			return self.playerHand

		def setPlayerHand(self, arr):
			self.playerHand = arr

		def getCash(self):
			return self.__cash

		def rollCash(self):
			x = random.randint(500, 5000)
			self.__cash = x

		def getPlayerNumber(self):
			return self.__playerNumber

		def getHandTotal(self):
			return self.__handTotal

		def displayHandTotal(self):
			print("Player ", self.__playerNumber, end = '')
			print("'s Hand Value: ", self.__handTotal, end = '\n')

		def addToHandTotal(self, num):
			self.__handTotal += num

		def resetHandTotal(self):
			self.__handTotal = 0

		def getBetTotal(self):
			return self.__bet

		def addToBetTotal(self, num):
			self.__bet += num

		def resetBetTotal(self):
			self.__bet = 0

		def wonBetBlackjack(self):
			self.__cash += self.__bet * 1.5

		def wonBet(self):
			self.__cash += self.__bet

		def lostBet(self):
			self.__cash -= self.__bet

	"""
		Program Methods 
		---------------
	""" 

	def createCard(s, r):

		tempCard = card('', '')

		suitArr = 'Spades', 'Hearts', 'Diamonds', 'Clubs'
		rankArr = 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'

		tempCard.setSuit(suitArr[s])
		tempCard.setRank(rankArr[r])
		tempCard.determineColor()

		return tempCard


	def createDeck():

		tempDeck = []

		for s in range(0, 4):
			for r in range(0, 13):
				tempDeck.append(createCard(s, r))

		for i in range(0, 3):
			random.shuffle(tempDeck)

		return tempDeck


	def createPlayer(numPlayer):

		tempPlayer = player(numPlayer)
		tempPlayer.rollCash()

		return tempPlayer


	def createGroup(numPlayers):

		tempGroup = []

		for n in range(0, numPlayers):
			tempGroup.append(createPlayer(n))

		return tempGroup


	def determineColor(tempCard):
		if tempCard.getSuit() == 'Spades' or tempCard.getSuit() == 'Clubs':
			return 'Black'
		elif tempCard.getSuit() == 'Hearts' or tempCard.getSuit() == 'Diamonds':
			return 'Red'


	def determineValue(tempCard):
		
		if tempCard.getRank() == 'Jack' or tempCard.getRank() == 'Queen' or tempCard.getRank() == 'King':
			return 10

		elif tempCard.getRank() == 'Ace':
			c = -1

			while not c == 1 or not c == 11:

				try:
					c = int(input('Do you want the ace to be a 1 or 11?: '))

					return c

				except ValueError:
					print("\nUser entered a char or alpha value instead of an integer!")

				except Exception:
					print("\nSomething unexpected went wrong!")

		else:
			return tempCard.getRank()

	def determineValueDealer(dealer, tempCard):
		if tempCard.getRank() == 'Jack' or tempCard.getRank() == 'Queen' or tempCard.getRank() == 'King':
			return 10

		elif tempCard.getRank() == 'Ace':
			
			if (dealer.getHandTotal()+11) <= 21:
				return 11
			else:
				return 1

		else:
			return tempCard.getRank()


	def checkStatusDealer(dealer, player):
		if dealer.getHandTotal() > 21:
			print('\nThe Dealer has bust!')
			if player.getHandTotal() < 21:
				print('\n', player.getHandTotal(), 'vs. Bust!')
				print('\nPlayer', player.getPlayerNumber(), 'has won the bet!')
				player.wonBet()

			elif player.getHandTotal() == 21:
				print('\n', player.getHandTotal(), ' vs. Bust!')
				print('\nPlayer', player.getPlayerNumber(), 'has won the bet!')
				player.wonBetBlackjack()

			else:
				print('\nBoth parties have bust!')
				print('\nPlayer', player.getPlayerNumber(), 'has lost the bet!')
				player.lostBet()
			return True

		elif player.getHandTotal() > 21:
			print('\n\nPlayer', player.getPlayerNumber(), 'has bust!')
			print('\nBust! vs.', dealer.getHandTotal())
			print('\nPlayer', player.getPlayerNumber(), 'has lost the bet!')
			player.canPlay = False
			player.lostBet()
			return False

		elif dealer.getHandTotal() == player.getHandTotal():
			print('\n', player.getHandTotal(), ' vs. ', dealer.getHandTotal())
			print('\nThe game ends in a draw!')
			return True

		elif dealer.getHandTotal() == 21:
			if player.getHandTotal() != 21:	
				print('\n', player.getHandTotal(), ' vs. ', dealer.getHandTotal())
				print('\nPlayer', player.getPlayerNumber(), 'has lost the bet!')
				player.lostBet()
			return True

		elif (dealer.getHandTotal() > player.getHandTotal()) and (not dealer.getHandTotal() > 21 and not player.getHandTotal() > 21):
			print('\n', player.getHandTotal(), ' vs. ', dealer.getHandTotal())
			print('\nPlayer', player.getPlayerNumber(), 'has lost the bet!')
			player.lostBet()
			return True

		elif (dealer.getHandTotal() < player.getHandTotal()) and (not dealer.getHandTotal() > 21 and not player.getHandTotal() > 21):
			print('\n', player.getHandTotal(), ' vs. ', dealer.getHandTotal())
			print('\nPlayer', player.getPlayerNumber(), 'has won the bet!')
			player.wonBet()
			return True


	def checkStatus(player, dealer):	# used to check if a "natural" has been dealt
		if player.getHandTotal() > 21:
			print('\nPlayer', player.getPlayerNumber(), 'has bust!')
			print('\n', player.getHandTotal(), ' vs. ', dealer.getHandTotal())
			print('\nPlayer', player.getPlayerNumber(), 'has lost the bet!')
			player.canPlay = False
			player.lostBet()
			return False

		elif player.getHandTotal() == 21:
			player.hasBlackjack = True
			if dealer.getHandTotal() != 21:
				print('\n', player.getHandTotal(), ' vs. ', dealer.getHandTotal())
				print('\nPlayer ', player.getPlayerNumber(), ' has won the bet!')
				player.wonBetBlackjack()
				return True
			else:
				return False
		else:
			return False

	"""
		Game Start
		----------
	""" 

	# MainGame Start

	def mainGame(player1, x):

		# initialize deck

		tempDeck = []
		tempShoeDeck = []

		dealerHand = []
		playerHand = []

		tempDealr = dealer()

		for i in range(1, 8):			# generates 8 decks of 52 pre-shuffled cards
			tempDeck = createDeck()
			tempShoeDeck += tempDeck

		for i in range(0, 3):			# shuffles the shoe 3 times
			random.shuffle(tempDeck)

		cardDrawn = tempShoeDeck.pop()	# deal one card to the player
		playerHand.append(cardDrawn)

		cardDrawn = tempShoeDeck.pop()	# deal one card to the dealer
		dealerHand.append(cardDrawn)

		cardDrawn = tempShoeDeck.pop()	# deal one more card to the player
		playerHand.append(cardDrawn)

		cardDrawn = tempShoeDeck.pop()	# deal one more card to the dealer
		dealerHand.append(cardDrawn)

		# start game

		# take in player bets

		c = -1

		while (c < 25 or c > player1.getCash()) or c == player1.getCash(): 	# checks the bet amount is feasible

			try:
				c = int(input('\nHow much would you like to bet? (Minimum $25): '))
				if c != player1.getCash():
					player1.addToBetTotal(c)

			except ValueError:
				print("\nUser entered a char or alpha value instead of an integer!")

			except Exception:
				print("\nSomething unexpected went wrong!")

			finally:
				if c == player1.getCash():
					print("\nPlayer cannot go all in!")

		# dealing begins

		print("\nThe Dealer's Hand:")

		for c in dealerHand:
			print(' - ', c)
			tempDealr.addToHandTotal(determineValueDealer(tempDealr, c))

		print(tempDealr)

		print("\nPlayer", player1.getPlayerNumber(), end = '')
		print("'s Hand:")

		for c in playerHand:
			print(' - ', c)

		for c in playerHand:
			player1.addToHandTotal(determineValue(c))

		print("\nP", end = '')
		print(player1.getPlayerNumber(), end = '')
		print("'s Hand:", player1.getHandTotal(), end = '  -  ')

		if player1.getHandTotal() == 21:
			print("\nThe player has a Blackjack!")
			if checkStatus(player1, tempDealr):
				return 0

		# splitFeasible = False

		doubleFeasible = True

		if player1.getBetTotal() * 2 > player1.getCash():
			doubleFeasible = False

		print("Bet: $", end = '')
		print(player1.getBetTotal(), "USD", end = '  -  ')
		print("In Bank: $", end = '') 
		print(player1.getCash(), "USD")

		print('\nOptions: 1. Hit', end = ' / ')
		print('2. Stand', end = ' ')

		numOptions = 2

		if doubleFeasible:
			print('/ 3. Double Down', end = ' ')
			numOptions = 3

		"""
		if playerHand[0].getRank() == playerHand[1].getRank():
			print('/ 4. Split')
			splitFeasible = True
			numOptions = 4
		"""

		c3 = -1

		while (c3 < 1 or c3 > numOptions): 

			try:
				c3 = int(input('\nWhat would you like to do?: '))

			except ValueError:
				print("\nUser entered a char or alpha value instead of an integer!")

			except Exception:
				print("\nSomething unexpected went wrong!")

		# Option 1: Hit 	(Finished)

		if c3 == 1:

			continueHit = True
			count = 2
			
			while continueHit:
				cardDrawn = tempShoeDeck.pop()	# deal one card to the player
				playerHand.append(cardDrawn)
				player1.addToHandTotal(determineValue(playerHand[count]))

				print('\n - ',playerHand[count])

				print("\nP", end = '')
				print(player1.getPlayerNumber(), end = '')
				print("'s Hand:", player1.getHandTotal(), end = '  ')

				count += 1

				if player1.getHandTotal() == 21:
					print('\nPlayer', player1.getPlayerNumber(), 'has 21!')
					checkStatusDealer(tempDealr, player1)
					return 0

				elif player1.getHandTotal() <= 21:

					c4 = -1

					while c4 < 1 or c4 > 2: 

						try:
							print("-  Bet: $", end = '')
							print(player1.getBetTotal(), "USD", end = '  -  ')
							print("In Bank: $", end = '') 
							print(player1.getCash(), "USD")

							print('\nOptions: 1. Hit / 2. Stand')

							c4 = int(input('What would you like to do?: '))

						except ValueError:
							print("\nUser entered a char or alpha value instead of an integer!")

						except Exception:
							print("\nSomething unexpected went wrong!")

						if c4 == 2:
							print('\nPlayer', player1.getPlayerNumber(), 'has decided to stand!')
							continueHit = False
				else:
					checkStatusDealer(tempDealr, player1)
					return 0

			# The Dealers Turn to hit

			if player1.getHandTotal() <= 21:
				print('\nThe Dealer will now choose to draw...')

			count = 2
			gameOverDealer = False

			if tempDealr.getHandTotal() < 17:
				print('The Dealer will draw!')
			else:
				print('The Dealer will not Draw!')
				gameOverDealer = True
			
			while not gameOverDealer and tempDealr.getHandTotal() < 17:
				cardDrawn = tempShoeDeck.pop()	# deal one card to the Dealer
				dealerHand.append(cardDrawn)
				tempDealr.addToHandTotal(determineValueDealer(tempDealr, dealerHand[count]))

				print('\n - ', dealerHand[count], '\n')

				print(tempDealr)

				count += 1

				if tempDealr.getHandTotal() >= 17:
					gameOverDealer = True

			checkStatusDealer(tempDealr, player1)


		# Option 2: Stand 	(Finished)

		elif c3 == 2:
			print('\nPlayer', player1.getPlayerNumber(), 'has decided to stand!')

			# The Dealers Turn to hit

			if player1.getHandTotal() <= 21:
				print('\nThe Dealer will now choose to draw...')

			count = 2
			gameOverDealer = False

			if not gameOverDealer and tempDealr.getHandTotal() < 17:
				print('The Dealer will draw!')

			if tempDealr.getHandTotal() > 16 and tempDealr.getHandTotal() < 21:
				print('The Dealer will not Draw!')
				gameOverDealer = True
			
			while not gameOverDealer and tempDealr.getHandTotal() < 17:
				cardDrawn = tempShoeDeck.pop()	# deal one card to the Dealer
				dealerHand.append(cardDrawn)
				tempDealr.addToHandTotal(determineValueDealer(tempDealr, dealerHand[count]))

				print('\n - ', dealerHand[count], '\n')

				print(tempDealr)

				count += 1

				if tempDealr.getHandTotal() >= 17:
					gameOverDealer = True

			checkStatusDealer(tempDealr, player1)


		# Option 3: Double Down

		elif c3 == 3:
			
			# The Player doubles his bet

			player1.addToBetTotal(player1.getBetTotal())

			print("\nThe total bet has doubled!: $", end = '')
			print(player1.getBetTotal(), "USD")

			cardDrawn = tempShoeDeck.pop()	# deal one last card to the player
			playerHand.append(cardDrawn)
			player1.addToHandTotal(determineValue(playerHand[2]))

			print('\n - ',playerHand[2],'\n')

			player1.displayHandTotal()

			if player1.getHandTotal() > 21:
				checkStatusDealer(tempDealr, player1)
				return 0
			else:	
				print('\nPlayer', player1.getPlayerNumber(), 'can no longer hit!')

			# The Dealers Turn to hit

			if player1.getHandTotal() <= 21:
				print('\nThe Dealer will now choose to draw...')

			count = 2
			gameOverDealer = False

			if not gameOverDealer and tempDealr.getHandTotal() < 17:
				print('The Dealer will draw!')

			if tempDealr.getHandTotal() > 16 and tempDealr.getHandTotal() < 21:
				print('The Dealer will not Draw!')
				gameOverDealer = True
			
			while not gameOverDealer and tempDealr.getHandTotal() < 17:
				cardDrawn = tempShoeDeck.pop()	# deal one card to the Dealer
				dealerHand.append(cardDrawn)
				tempDealr.addToHandTotal(determineValueDealer(tempDealr, dealerHand[count]))

				print('\n - ', dealerHand[count], '\n')

				print(tempDealr)

				count += 1

				if tempDealr.getHandTotal() >= 17:
					gameOverDealer = True

			checkStatusDealer(tempDealr, player1)


		# Option 4: Split

		#elif c3 == 4:
		#	print('')
	

	# MainGame End

	# MainMultiGame Begin

	def mainMultiGame(playerArr, x):
		
		# initialize deck

		tempDeck = []
		tempShoeDeck = []

		dealerHand = []
		playerHand = []

		playerOneHand = []
		playerTwoHand = []
		playerThreeHand = []
		playerFourHand = []
		playerFiveHand = []
		playerSixHand = []

		tempDealr = dealer()

		for i in range(1, 8):			# generates 8 decks of 52 pre-shuffled cards
			tempDeck = createDeck()
			tempShoeDeck += tempDeck

		for i in range(0, 3):			# shuffles the shoe 3 times
			random.shuffle(tempDeck)

		# take in player bets

		print("\n - Minimum $25 or bet $0 to sit out this game - ")

		for p in playerArr:

			c = -1

			if p.getCash() < 25:
				p.canPlay = False
				p.sitOut = True

			elif p.getCash() >= 25:
				p.canPlay = True
				p.sitOut = False

			while (c and (c < 25 or c > p.getCash()) and p.canPlay) or c == p.getCash(): 	# checks the bet amount is feasible

				print(p)
				print("P", end = '')
				print(p.getPlayerNumber(), end = '')
				print("'s", end = ' ')

				try:
					c = int(input('bet?: '))
					if c != p.getCash():
						p.addToBetTotal(c)
					else:
						print("\nPlayer cannot go all in!")

				except ValueError:
					print("\nUser entered a char or alpha value instead of an integer!")

				except Exception:
					print("\nSomething unexpected went wrong!")

			if c == 0:
				p.canPlay = False
				p.sitOut = True

		# start dealing

		for p in playerArr:
			if p.canPlay:
				print('\nPlayer', p.getPlayerNumber(), end = '')
				print(':')
				for i in range(0, 2):
					cardDrawn = tempShoeDeck.pop()	# deal one card to the player
					playerHand.append(cardDrawn)
					p.addToHandTotal(determineValue(playerHand[i]))
					print(' - ', playerHand[i])
				print(" - P", end = '')
				print(p.getPlayerNumber(), end = '')
				print("'s Hand:", p.getHandTotal(), end = '')

				if p.getPlayerNumber() == 1:
					playerOneHand = playerHand
				elif p.getPlayerNumber() == 2:
					playerTwoHand = playerHand
				elif p.getPlayerNumber() == 3:
					playerThreeHand = playerHand
				elif p.getPlayerNumber() == 4:
					playerFourHand = playerHand
				elif p.getPlayerNumber() == 5:
					playerFiveHand = playerHand
				elif p.getPlayerNumber() == 6:
					playerSixHand = playerHand

				playerHand.clear()

		for f in range(0, 2):
			cardDrawn = tempShoeDeck.pop()	# deal one card to the dealer
			dealerHand.append(cardDrawn)

		print("\nThe Dealer's Hand:")

		for c in dealerHand:
			print(' - ', c)
			tempDealr.addToHandTotal(determineValueDealer(tempDealr, c))

		print(tempDealr)

		for p in playerArr:

			if p.canPlay:
				print('\nPlayer', p.getPlayerNumber(), end = '')
				print("'s Turn:", end = '\n')

				print("P", end = '')
				print(p.getPlayerNumber(), end = '')
				print("'s Hand:", p.getHandTotal(), end = '  ')

				if p.getHandTotal() == 21:
					print("\n\nThe player has a Blackjack!")
					if checkStatus(p, tempDealr):
						p.canPlay = False
						p.sitOut = True

				if p.canPlay:
					doubleFeasible = True

					if p.getBetTotal() * 2 > p.getCash():
						doubleFeasible = False

					print("-  Bet: $", end = '')
					print(p.getBetTotal(), "USD", end = '  -  ')
					print("In Bank: $", end = '') 
					print(p.getCash(), "USD")

					print('\nOptions: 1. Hit', end = ' / ')
					print('2. Stand', end = ' ')

					numOptions = 2

					if doubleFeasible:
						print('/ 3. Double Down', end = ' ')
						numOptions = 3

					c3 = -1

					while (c3 < 1 or c3 > numOptions): 

						try:
							c3 = int(input('\nWhat would you like to do?: '))

						except ValueError:
							print("\nUser entered a char or alpha value instead of an integer!")

						except Exception:
							print("\nSomething unexpected went wrong!")

					# Option 1: Hit

					if c3 == 1:

						continueHit = True

						if p.getPlayerNumber() == 1:
							playerHand = playerOneHand
						elif p.getPlayerNumber() == 2:
							playerHand = playerTwoHand
						elif p.getPlayerNumber() == 3:
							playerHand = playerThreeHand
						elif p.getPlayerNumber() == 4:
							playerHand = playerFourHand
						elif p.getPlayerNumber() == 5:
							playerHand = playerFiveHand
						elif p.getPlayerNumber() == 6:
							playerHand = playerSixHand
			
						while continueHit and p.canPlay:

							#for c in playerHand:
								#print('\n - ', c)

							cardDrawn = tempShoeDeck.pop()	# deal one card to the player
							playerHand.append(cardDrawn)
							p.addToHandTotal(determineValue(playerHand[len(playerHand)-1]))

							print('\n - ',playerHand[len(playerHand)-1])

							print("\nP", end = '')
							print(p.getPlayerNumber(), end = '')
							print("'s Hand:", p.getHandTotal(), end = '  ')

							if p.getHandTotal() == 21:
								print('\nPlayer', p.getPlayerNumber(), 'has 21!')
								continueHit = False
								if tempDealr.getHandTotal() == 21:
									p.canPlay = False
									continueHit = False

							elif p.getHandTotal() <= 21:

								c4 = -1

								while c4 < 1 or c4 > 2: 

									try:
										print("-  Bet: $", end = '')
										print(p.getBetTotal(), "USD", end = '  -  ')
										print("In Bank: $", end = '') 
										print(p.getCash(), "USD")

										print('\nOptions: 1. Hit / 2. Stand')

										c4 = int(input('What would you like to do?: '))

									except ValueError:
										print("\nUser entered a char or alpha value instead of an integer!")

									except Exception:
										print("\nSomething unexpected went wrong!")

									if c4 == 2:
										print('\nPlayer', p.getPlayerNumber(), 'has decided to stand!')
										continueHit = False
							elif p.getHandTotal() > 21:
								print('\nPlayer', p.getPlayerNumber(), 'has bust!')
								p.canPlay = False

					# Option 2: Stand

					elif c3 == 2:
						print('\nPlayer', p.getPlayerNumber(), 'has decided to stand!')

					###


					# Option 3: Double Down

					elif c3 == 3:
			
						# The Player doubles his bet

						p.addToBetTotal(p.getBetTotal())

						print("\nThe total bet has doubled!")

						cardDrawn = tempShoeDeck.pop()	# deal one last card to the player
						playerHand.append(cardDrawn)
						p.addToHandTotal(determineValue(playerHand[len(playerHand)-1]))

						print('\n - ',playerHand[len(playerHand)-1])

						print("\nP", end = '')
						print(p.getPlayerNumber(), end = '')
						print("'s Hand:", p.getHandTotal(), end = '  ')
						print("-  Bet: $", end = '')
						print(p.getBetTotal(), "USD")

						if p.getHandTotal() > 21:
							checkStatusDealer(tempDealr, p)
						else:	
							print('\nPlayer', p.getPlayerNumber(), 'can no longer hit!')

				playerOneHand = []
				playerTwoHand = []
				playerThreeHand = []
				playerFourHand = []
				playerFiveHand = []
				playerSixHand = []

				###			

		# The Dealers Turn to hit

		print('\nThe Dealer will now choose to draw...')

		count = 2
		gameOverDealer = False

		if tempDealr.getHandTotal() < 17:
			print('The Dealer will draw!')
		else:
			print('The Dealer will not Draw!')
			gameOverDealer = True
			
		while not gameOverDealer and tempDealr.getHandTotal() < 17:
			cardDrawn = tempShoeDeck.pop()	# deal one card to the Dealer
			dealerHand.append(cardDrawn)
			tempDealr.addToHandTotal(determineValueDealer(tempDealr, dealerHand[count]))

			print('\n - ', dealerHand[count], '\n')

			print(tempDealr)

			count += 1

			if tempDealr.getHandTotal() >= 17:
				gameOverDealer = True

		for p in playerArr:
			if not p.sitOut:
				checkStatusDealer(tempDealr, p)
				p.resetHandTotal()
				p.resetBetTotal()

	# Multiplayer Game End

	continued = True

	while continued:

		broke = False
		
		print('\n Black Jack Main Menu ')
		print('----------------------')
		print('1. Single Player Game ')
		print('2. Multiplayer Game')
		print('3. Quit Program')

		c1 = -1

		while c1 < 1 or c1 > 3:

			try:
				c1 = int(input('\nWhat would you like to do: '))

			except ValueError:
				print("\nUser entered a char or alpha value instead of an integer!")

			except Exception:
				print("\nSomething unexpected went wrong!")

		# Option 5: Quit the Program

		if c1 == 3:
			print('\n\tGood Bye!\n')
			continued = False

		# Option 1: Single Player Game

		elif c1 == 1:

			playNum = 1
			playAgain = True

			p1 = player(playNum)
			p1.rollCash()

			while not broke and playAgain:

				print('\nThis table has', p1.getPlayerNumber(), 'player(s)', end = '\n')
				print(p1)

				#
				mainGame(p1, p1.getPlayerNumber())

				p1.resetHandTotal()
				p1.resetBetTotal()

				#

				if p1.getCash() <= 50:
					broke = True

				c2 = -1

				while (c2 < 1 or c2 > 2) and not broke:

					try:
						c2 = int(input('\nWould you like to play again?\n1. Yes / 2. No: '))

					except ValueError:
						print("\nUser entered a char or alpha value instead of an integer!")

					except Exception:
						print("\nSomething unexpected went wrong!")

					if c2 == 2:
						playAgain = False

				if broke:
					print('\nYou dont have enough funds to continue!\n\t    Game Over!!!')

		# Option 2: Multiplayer Game

		elif c1 == 2:

			allBroke = False

			playAgain = True

			playNum = 1

			if not broke and playAgain:

				c2 = -1

				while c2 < 2 or c2 > 6:

					try:
						c2 = int(input('\nHow many players will play? (2 - 6): '))

					except ValueError:
						print("\nUser entered a char or alpha value instead of an integer!")

					except Exception:
						print("\nSomething unexpected went wrong!")

				# make an group (array) of players

				tempPlayer = []
				tempGroup = []

				for i in range(1, c2+1):
					tempPlayer = createPlayer(i)
					tempGroup.append(tempPlayer)
					playNum+=1

			while not allBroke and playAgain:

				print('\nThis table has', playNum-1, 'player(s)', end = '\n')

				mainMultiGame(tempGroup, playNum)

				count = 0

				for p in tempGroup:
					if p.getCash() <= 50:
						count+=1
					if count == playNum-1:
						print("\nAll players do not have enough funds to continue!\n\t\t    Game Over!!!")
						allBroke = True

				c2 = -1

				while (c2 < 1 or c2 > 2) and not allBroke:

					try:
						c2 = int(input('\nWould you like to play again?\n1. Yes / 2. No: '))

					except ValueError:
						print("\nUser entered a char or alpha value instead of an integer!")

					except Exception:
						print("\nSomething unexpected went wrong!")

				if c2 == 2:
					playAgain = False

			#print(c2)

		# main ends

"""
	Main Program Method Call 
""" 

main()

"""
cardLibrary = { 
			
			'Spades' : 'Ace', 'Spades' : '2', 'Spades' : '3', 
			'Spades' : '4', 'Spades' : '5', 'Spades' : '6', 'Spades' : '7',
			'Spades' : '8', 'Spades' : '9', 'Spades' : '10', 'Spades' : 'Jack', 
			'Spades' : 'Queen', 'Spades' : 'King',

			'Hearts' : 'Ace', 'Hearts' : '2', 'Hearts' : '3', 
			'Hearts' : '4', 'Hearts' : '5', 'Hearts' : '6', 'Hearts' : '7',
			'Hearts' : '8', 'Hearts' : '9', 'Hearts' : '10', 'Hearts' : 'Jack', 
			'Hearts' : 'Queen', 'Hearts' : 'King',

			'Diamonds' : 'Ace', 'Diamonds' : '2', 'Diamonds' : '3', 
			'Diamonds' : '4', 'Diamonds' : '5', 'Diamonds' : '6', 'Diamonds' : '7',
			'Diamonds' : '8', 'Diamonds' : '9', 'Diamonds' : '10', 'Diamonds' : 'Jack', 
			'Diamonds' : 'Queen', 'Diamonds' : 'King',

			'Clubs' : 'Ace', 'Clubs' : '2', 'Clubs' : '3', 
			'Clubs' : '4', 'Clubs' : '5', 'Clubs' : '6', 'Clubs' : '7',
			'Clubs' : '8', 'Clubs' : '9', 'Clubs' : '10', 'Clubs' : 'Jack', 
			'Clubs' : 'Queen', 'Clubs' : 'King' } 

"""


			