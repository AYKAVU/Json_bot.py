from telebot import TeleBot, types
import json

bot = TeleBot(token='YOUR TOKEN', parse_mode='html')


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Я умею проверять JSON и форматировать его в красивый текст\nВведи JSON в виде строки:',
    )
@bot.message_handler()
def message_handler(message: types.Message):
    try:
        payload = json.loads(message.text)
    except json.JSONDecodeError as ex:
        bot.send_message(
            chat_id=message.chat.id,
            text=f'При обработке произошла ошибка:\n<code>{str(ex)}</code>'
        )
        return

    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'JSON:\n<code>{text}</code>'
    )
DEFINITOINS = {
    'регресс': 'Вид тестирования, при котором мы проверяем, что новый функционал не сломал существующий',
    'новое слово': 'тут его определение',
}

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id, 
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс',
    )
@bot.message_handler()
def message_handler(message: types.Message):
    definition = DEFINITOINS.get(
        message.text.lower(),
    )
    if definition is None:
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        return

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()
