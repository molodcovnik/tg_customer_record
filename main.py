from config import *
from sql_commands import register_user, start_base, record_user, check_record, show_empty_slots

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = token




# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)
#
#     await message.answer(message.text)

@dp.message_handler(commands=['reg'])
async def registration(message: types.Message):
    uid = message.from_user.id
    register_user(uid)
    # answer = register_user()
    await message.answer('Теперь вы зарегистрированны')


@dp.message_handler(commands=['empty'])
async def writing_on(message: types.Message):
    results = show_empty_slots()
    if results:
        for result in results:
            await message.answer(f'{result[2]} {result[3]}')
    else:
        await message.answer(f'Свободных мест нет на ближайшие дни...')

@dp.message_handler(content_types=['text'])
async def record(message: types.Message):
    values = message.text.split()
    name = values[0]
    date = values[1]
    time = values[2]
    if check_record(date, time) is True:
        await message.answer('На это время уже есть запись, выберете другое время')
    else:
        record_user(name, date, time)
        await message.answer(f'Уважаемый {name} вы записаны на {date} {time}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_base())
