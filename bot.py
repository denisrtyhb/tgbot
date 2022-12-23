import os
from telebot.async_telebot import AsyncTeleBot
import asyncio
import notifier

from solve_line import solve_linear_impl

from evoke import evoke_impl

from note import note_impl, note_statistics_impl

from random import randint
from bulls_and_cows import bulls_and_cows_impl

from year_percentage import time_to_percent


def readToken():
	token = None
	if not os.path.exists("token"):
		token = input("Token not found, please write it:")
		with open("token", "w") as file:
			file.write(token)
	else:
		with open("token", "r") as file:
			token = file.read()
	return token



TOKEN = readToken()

bot = AsyncTeleBot(TOKEN)

#chat_member_handler. When status changes, telegram gives update. check status from old_chat_member and new_chat_member.
@bot.message_handler(commands=['h', 'help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I have exactly 5 use scenarios
1) I can solve linear equations with /solve
2) I can say, how much of the year is passed with /remind_year, so you don't feel lost in inevatable flow of time
3) I can evoke memories to your mind, with /evoke
4) I can take notes with tags with /note and send statistics with /note_statistics
5) I can play 'bulls and cows' game with /play
""")

async def main():
    await bot.polling(none_stop=True, interval=0)

state = dict() # dialog_id -> [scenario_number, some_info]

@bot.message_handler(commands=['stop', 'exit'])
async def stop(message):
    state[message.chat.id] = [0]


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(commands=['solve'])
async def solve_linear(message):
    state[message.chat.id] = [1]
    await bot.reply_to(message, 'I am ready to solve linear equations. Just write them')

@bot.message_handler(commands=['evoke'])
async def evoke(message):
    state[message.chat.id] = [2, message.chat.id]
    await bot.reply_to(message, 'Write the memory you need to evoke soon')

@bot.message_handler(commands=['note'])
async def note(message):
    state[message.chat.id] = [3, message.chat.id]
    await bot.reply_to(message, 'Ready to take notes. Write tag:')

@bot.message_handler(commands=['note_statistics'])
async def note_statistics(message):
    state[message.chat.id] = [4, message.chat.id]
    await bot.reply_to(message, 'Ready to write statistics. Write tag:')

@bot.message_handler(commands=['play'])
async def bulls_and_cows(message):
    state[message.chat.id] = [5, randint(0, 9999), 0]
    await bot.reply_to(message, 'I am ready to play the game. Just write any 4 digit number')

@bot.message_handler(commands=['remind_year'])
async def note_statistics(message):
    state[message.chat.id] = [0]
    await bot.reply_to(message, f'''
It is {time_to_percent()} of year now''')

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    print("id -", message.chat.id)
    if message.chat.id not in state or state[message.chat.id][0] == 0:
        await bot.reply_to(message, "I don't have active jobs yet. Write /help if don't know what to do")
    else:
    	now_state = state[message.chat.id]
    	function_list = [
    	    solve_linear_impl,
    	    evoke_impl,
    	    note_impl,
    	    note_statistics_impl,
    	    bulls_and_cows_impl]
    	if now_state[0] == 0:
    		pass
    	if 1 <= now_state[0] and now_state[0] <= 6:
    		await bot.reply_to(message, function_list[now_state[0] - 1](message.text, now_state))
    	else:
    		await bot.reply_to(message, "invalid state")

async def notify():
    while True:
        print(notifier.job_list)
        while len(notifier.job_list) != 0 and notifier.job_list[-1].time < notifier.tm.time():
            print(1)
            await bot.send_message(notifier.job_list[-1].dialog_id, notifier.job_list[-1].text)
            print(2)
            notifier.job_list.pop()
            print(3)
            break
        print("ended")
        await asyncio.sleep(1)
    await print(10)

background_tasks = set()
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    main_task = loop.create_task(main())
    background_tasks.add(main_task)
    main_task.add_done_callback(background_tasks.discard)


    task2 = loop.create_task(notify())
    background_tasks.add(task2)
    task2.add_done_callback(background_tasks.discard)

    loop.run_until_complete(asyncio.wait(background_tasks))
    loop.close()


print("lmao")