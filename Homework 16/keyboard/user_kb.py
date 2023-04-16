from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton,  KeyboardButton

# function buttons
b1 = KeyboardButton('/Случайный_анекдот😄')
b2 = KeyboardButton('/Анекдот_из_сохраненных⭐')

kb_client = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
kb_client.row(b1).row(b2)


inline_b1 = InlineKeyboardButton("Сохранить💾", callback_data='save_joke', )
inline_kb = InlineKeyboardMarkup().add(inline_b1)


