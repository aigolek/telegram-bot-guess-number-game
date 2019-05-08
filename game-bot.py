import telebot
from telebot import types
import credentials as game

new_echo_bot = telebot.TeleBot("xxx") 
guess_game = game.GuessGame()

@new_echo_bot.message_handler(content_types=['text'])
def handle_start_game(message):
    # global guess_game
    chat_id = message.chat.id
    text = message.text
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton("Let's play!")
    itembtn2 = types.KeyboardButton("Show me correct answer")
    markup.add(itembtn1, itembtn2)
    
    if text == "Let's play!":
        new_echo_bot.reply_to(message, guess_game.start_game())
    elif text == "Show me correct answer":
        new_echo_bot.reply_to(message, guess_game.show_answer())
    else: 
        msg = guess_game.guess_number(int(message.text))
        new_echo_bot.send_message(message.chat.id, msg)  

new_echo_bot.polling()    