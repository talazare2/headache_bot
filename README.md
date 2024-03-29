Headache-checker
-------------------------------------------------------------------------
проект телеграмм бота на базе aiogram 3.0, который позволяет отслеживать головные боли пользователя. 
Ежедневно пользователю будет приходить небольшой опрос о его самочувствии, на основании которого будет строиться статистика частоты головных болей, 
кроме того на основании корелляций будут выявляться некоторые критерии, влияющие на возникновение головной боли, 
на ее локализацию и на интенсивность боли.

Общение с ботом возможно на трех основных языках: русский, английский, французский. 
Выбор языка осуществляется при первом запуске бота.
Для определения погоды боту требуется разрешение на геолокацию устройства. 
Определение положения устройства по названию города не рационально, так как небольшие населенные пункты зачастую имеют одинаковые названия, 
погода в ближайших крупных населенных пунктах может знасительно отличаться, а почтовый индекс помнят не все, 
кроме того можно запутаться в индексах для разных стран.

--------------------------------------------------------------------------

Основные команды:
---------------------------------------------------------------------------

/start - запуск бота

/help - инструкция взаимодействия с ботом

/abort - прервать работу бота

/report - составить отчет по данным о головных болях пользователя

---------------------------------------------------------------------------
Структура кода:
---------------------------------------------------------------------------

Необходимые пакеты: requirements.txt

Точка входа (запуск бота): main_bot.py

API токены и прочие секреты: .env (не выкладывается на гитхаб)

Пример нерабочего .env файла: .env.example

config_data: пакет с модулем конфигурации бота

handlers: пакет с модулями взаимодействия с пользователем (обработка команд)

keybords: пакет с модулем для создания инлайн-кнопок

lexicon: пакет со словарями команд и диалогами

external_services: пакет с модулями для работы с внешними API 

database: пакет с модулем для создания баз данных пользователя и для их хранения

analysis: пакет с модулями для обработки данных и создания отчетов

test: пакет с тестовой базой данных для проверки работы модуля анализа данных

-----------------------------------------------------------------------------
