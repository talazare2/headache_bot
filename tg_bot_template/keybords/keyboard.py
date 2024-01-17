from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
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