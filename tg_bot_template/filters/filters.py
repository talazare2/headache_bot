from typing import Dict, Union, Any
from aiogram.filters import Filter
from aiogram.types import Message


class FilterAD(Filter):

    async def __call__(self, message : Message) -> Union[bool, Dict[str, Any]]:
        try:
            mes_list = list(map(int, message.text.split('/')))
            print(mes_list)
            if mes_list[0] < mes_list[1]:
                return False
            if (mes_list[0] < 60) or (mes_list[0] > 300):
                return False
            if (mes_list[1] < 30) or (mes_list[1] > 250):
                return False
            return message.text
        except:
            return False