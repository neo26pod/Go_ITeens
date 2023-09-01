import random
import logging, os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


motiv = {
    'Спорт': {
        '1': 'Неважливо, як повільно ти просуваєшся. Головне – ти не зупиняєшся.',
        '2': 'Спортсмен не може бігати з грошима в кишенях. Він повинен бігти з надією в серці і мріями в голові.',
        '3': 'Якщо ти хочеш бути кращим за інших, то приготуйся робити те, що інші не хочуть робити.',
        '4': 'Сила волі – це м’яз, який потребує тренувань, точно так само, як і м’язи тіла.',
        '5': 'Переможе не той, хто сильніший, а той, хто готовий йти до кінця.',
        '6': 'Зробіть хоча б раз те, що, за словами оточуючих, вам не по плечу. Після цього ви вже ніколи не будете звертати увагу на їхні правила і обмеження.',
        '7': 'Не тікайте від виклику. Замість цього біжіть до нього, тому що єдиний спосіб уникнути страху – розтоптати його під ногами.',
        '8': 'Досконалість – це не одиничний акт, а звичка. Ви – це те, що ви робите багато разів.',
        '9': 'Перемагай свою лінь і ти переможець!',
        '10': 'Ви не програли, поки не перестанете намагатися.'
    },
    'Навчання': {
        '1': 'Навчання – це не час. Навчання – це зусилля.',
        '2': 'Біль вчення лише тимчасова. Біль незнання – невігластво – вічна.',
        '3': 'Життя – це не тільки навчання, але якщо ти не можеш пройти навіть через цю її частину, як ти будеш знати, на що здатний?',
        '4': 'Успіх – це сходи, на які не піднятися, тримаючи руки в кишенях.',
        '5': 'Якщо ви працюєте над поставленими цілями, то ці цілі будуть працювати на вас.',
        '6': 'Секрет успіху – знати те, що ніхто ще не знає.',
        '7': 'Навіть зараз твої суперники гортають розумні книги.',
        '8': 'Помилки здійснювати не страшно. Головне кожен раз помилятися в чомусь новому.',
        '9': 'Між успіхом і невдачею лежить прірва, ім’я якої «у мене немає часу».',
        '10': 'Якість ніколи не є випадковою, це завжди результат зусилля інтелекту '
    },
    'Подорожі': {
        '1': 'Говорити на іноземній мові – значить завоювати його світ і культуру.',
        '2': 'Подорожі згубні для забобонів, фанатизму й обмеженості, ось чому вони так гостро необхідні багатьом.',
        '3': 'Ніщо так не розвиває розум, як подорож.',
        '4': 'Життя під час подорожі – це мрія в чистому вигляді',
        '5': 'Інвестиції в поїздки це інвестиції в себе.',
        '6': 'Час, втрачений із задоволенням, не вважається втраченим.',
        '7': 'Подорожі вчать більше, ніж що б то не було. Іноді один день, проведений в інших місцях, дає більше, ніж десять років життя вдома.',
        '8': 'Для насолоди повнотою життя, потрібно безперервно бути в стані руху, тільки в такому випадку один день буде відрізнятися від іншого.',
        '9': 'Не відмовляйте собі в тому, що можете собі дозволити.',
        '10': 'Коли дійдеш до вершини, продовжуй сходження.'
    },
    'Успіх': {
        '1': 'Варто тільки повірити, що ви можете – і ви вже на півдорозі до мети.',
        '2': 'Ваш час обмежений, не витрачайте його, живучи чужим життям',
        '3': 'Якщо ви хочете мати те, що ніколи не мали, вам доведеться робити те, що ви ніколи не робили.',
        '4': 'Коли ви знаєте, чого хочете, і ви хочете цього достатньо сильно, ви знайдете спосіб отримати це.',
        '5': 'Постарайтеся отримати те, що любите, інакше доведеться полюбити те, що отримали.',
        '6': 'Коли проблеми тягнуть вниз, дивися вгору.',
        '7': 'Пробуйте і зазнаєте невдачі, але не переривайте ваших старань.',
        '8': 'Наш великий недолік в тому, що ми надто швидко опускаємо руки. Найбільш вірний шлях до успіху – весь час пробувати ще один раз.',
        '9': 'Дозвольте собі розкіш не спілкуватися з неприємними людьми.',
        '10': 'Зроби життя навколо себе красивим. І нехай кожна людина відчує, що зустріч з тобою – це дар.'
    }
}
TOKEN = os.getenv('5800418391:AAGTEunt-IeHSjBILWaPJDZf9eW3bW70yaE')
logging.basicConfig(level=logging.INFO)
bot = Bot(token='5800418391:AAGTEunt-IeHSjBILWaPJDZf9eW3bW70yaE')
dp = Dispatcher(bot, storage=MemoryStorage())
ADMINS = []


@dp.message_handler(commands='start')
async def start(message: types.Message):
    motivation_choice = InlineKeyboardMarkup()
    for mot in motiv:
        button = InlineKeyboardButton(text=mot, callback_data=mot)
        motivation_choice.add(button)
    await message.answer(text='Привіт, Я - мотиваційний бот,\n Обери тему для мотивації:',
                         reply_markup=motivation_choice)
continue_keyboard = InlineKeyboardMarkup()
continue_button = InlineKeyboardButton(text="Продовжити", callback_data="continue")
finish_button = InlineKeyboardButton(text="Завершити", callback_data="finish")
continue_keyboard.add(continue_button, finish_button)

@dp.callback_query_handler()
async def get_motiv_info(callback_query: types.CallbackQuery, state: FSMContext, motivation_choice=InlineKeyboardMarkup()):
    print(callback_query.data)
    if callback_query.data in motiv.keys():
        main_motivation = random.randint(1, len(motiv[callback_query.data]))
        main = motiv[callback_query.data][str(main_motivation)]
        await bot.send_message(callback_query.message.chat.id, main)
        await bot.send_message(callback_query.message.chat.id, "Що б ви хотіли зробити далі?",
                           reply_markup=continue_keyboard)
    elif callback_query.data == "continue":
        await bot.send_message(callback_query.message.chat.id, "Оберіть наступну тему для мотивації:",
                           reply_markup=motivation_choice)
    elif callback_query.data == "finish":
        await bot.send_message(callback_query.message.chat.id, "Дякую за використання мотиваційного бота!")
        await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
