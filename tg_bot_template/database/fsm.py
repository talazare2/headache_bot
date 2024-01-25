from typing import Dict
from aiogram.fsm.state import State, StatesGroup

usr_dict = {}
# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    fill_lang = State()
    fill_start = State()
    fill_go = State()
    fill_go_2 = State()
    fill_lvl = State()       
    fill_loc = State()  
    fill_side = State()      
    fill_side = State()      
    fill_alc = State()   
    fill_presyn = State()   
    fill_press = State()
    fill_fev = State()
    fill_sleep = State()
    fill_meteo = State()