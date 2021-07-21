import telebot
import random

bot = telebot.TeleBot("")

@bot.message_handler()
def send_welcome(message):
	if (message.text=="/start") or (message.text=="help"):
		bot.send_message(message.from_user.id, "If u want to play /game")
	elif (message.text=="/game"):
		game(message)
	else:
		bot.send_message(message.from_user.id, "I don't undestand u")

@bot.message_handler(commands=['game'])
def game(message):
	try:
		lives = 10

		word_wariants = ["frog", "lollipop","anastasiya","yana", "beer", "dog", "cat", "hamster"]

		words_right = random.choice(word_wariants)

		word_in_g = "_" * len(words_right)

		sendit = "Lives amount:" + str(lives) + ". \nWord: " + word_in_g

		msg = bot.send_message(message.from_user.id, sendit)
		bot.register_next_step_handler(msg, ggg, lives, word_in_g, words_right)
	except:
		msg44 = bot.send_message(message.from_user.id, "Please write /game")
		bot.register_next_step_handler(msg44, game, lives, word_in_g, words_right)

@bot.message_handler()
def ggg(message, lives, word_in_g, words_right):
	try:
		if (len(message.text) == 1) and (message.text.islower()):
			letter = message.text

			ird = 0

			if letter in words_right:
				ird = 1
				bot.send_message(message.from_user.id, "You are right")
				index = -1
				while word_in_g.count(letter) != words_right.count(letter):
					index = words_right.find(letter, index + 1)
					word_in_g = word_in_g[:index:] + letter + word_in_g[(index + 1):]
				msg1 = bot.send_message(message.from_user.id, word_in_g)
			else:
				lives -= 1
				ird = 2
				kkk = "Try one more time\nLives: " + str(lives)
				msg2 = bot.send_message(message.from_user.id, kkk )
		else:
			ird = 3
			msg3 = bot.send_message(message.from_user.id, "Please write only one letter in lowercase (1)")
		if (lives > 0) and ("_" in word_in_g):
			if ird == 1:
				msgr = msg1
			elif ird == 2:
				msgr = msg2
			elif ird == 3:
				msgr = msg3
			bot.register_next_step_handler(msgr, ggg, lives, word_in_g, words_right)
		elif (lives > 0):
			bot.send_message(message.from_user.id, "You win! You can start new game /game\n")
		else:
			lll = "You lose:( You can ctart new game /game\nWord: " + words_right
			bot.send_message(message.from_user.id, lll )
	except:
		msg44 = bot.send_message(message.from_user.id, "Please write only one letter in lowercase (2)")
		bot.register_next_step_handler(msg44, ggg, lives, word_in_g, words_right)

bot.polling()