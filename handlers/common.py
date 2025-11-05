from aiogram import Router, F
from aiogram.types import Message
from keyboards.reply import main_menu, games_menu

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Добро пожаловать!", reply_markup=main_menu)

@router.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer("если нужна инфа об играх, просто нажми на кнопку 'о боте'")

@router.message(F.text == "🎮 Игры")
async def show_games(message: Message):
    await message.answer("Выберите игру:", reply_markup=games_menu)

@router.message(F.text == "ℹ️ О боте")
async def about_bot(message: Message):
    await message.answer(
        "🤖 Это бот с двумя играми и читалкой:\n\n"
        "✂️ <b>Камень, ножницы, бумага</b>\n"
        "— Выбери один из трёх вариантов.\n"
        "— Бот тоже делает выбор.\n"
        "— Камень побеждает ножницы, ножницы — бумагу, бумага — камень.\n\n"
        "🎲 <b>Угадай число на кубике</b>\n"
        "— Выбери число от 1 до 6.\n"
        "— Бот «бросает» кубик.\n"
        "— Если угадал — победа! 🎯\n\n"
        "Читай, играй и веселись! 😊",
        reply_markup=main_menu,
        parse_mode="HTML"
    )

@router.message(F.text == "📖 Читалка Ведьмака")
async def witcher_reader(message: Message):
    await message.answer("Раздел 'Читалка Ведьмака' в разработке 🏗️", reply_markup=main_menu)

# УБЕДИТЕСЬ, что этот обработчик НЕ перехватывает числа
# Если он есть - он должен быть ТОЛЬКО для действительно неизвестных сообщений
@router.message()
async def handle_unknown(message: Message):
    # Этот обработчик должен срабатывать только если другие не обработали сообщение
    await message.answer(
        "Извините, я не понимаю это сообщение.\nПожалуйста, используйте кнопки меню.",
        reply_markup=main_menu
    )