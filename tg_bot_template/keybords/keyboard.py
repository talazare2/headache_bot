from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON

# Function to create on-the-fly inline keyboard
def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Initialize builder
    kb_builder = InlineKeyboardBuilder()
    # Initialize list for buttons
    buttons: list[InlineKeyboardButton] = []

    # Fill list of buttons
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Unpack list to builder
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------
def yes_no_kb(lang):
    button_yes = KeyboardButton(text=LEXICON[lang]['yep'])
    button_no = KeyboardButton(text=LEXICON[lang]['nope'])

    # Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
    yes_no_kb_builder = ReplyKeyboardBuilder()

    # Добавляем кнопки в билдер с аргументом width=2
    yes_no_kb_builder.row(button_yes, button_no, width=2)

     # Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
    yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
        one_time_keyboard=True, 
        resize_keyboard=True)
    return yes_no_kb

# ------- Создаем кнопку геопозиции -------
def loc_kb(lang):
    button_1 = KeyboardButton(text=LEXICON[lang]['share_loc'], request_location=True)
    loc_kb = ReplyKeyboardMarkup(
        keyboard=[[button_1]], resize_keyboard=True, 
                  one_time_keyboard=True
    )
    return loc_kb