import telegram

api_key = '' #TOKEN 

bot = telegram.Bot(token=api_key)

 chat_id = bot.get_updates()[-1].message.chat_id
# chat_id = '' #chat_id
# print(chat_id)

bot.sendMessage(chat_id = chat_id, text="heeya 안녕!!")