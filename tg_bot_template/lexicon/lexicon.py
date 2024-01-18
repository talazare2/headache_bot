from typing import Dict


LEXICON_EN: Dict[str, str] = {
    '/help': 'Just type /start',
    '/abort': 'You cancelled your headache-check for today, see you tomorrow!',
    'begin': 'Let\'s start!',
    'stop': 'Not today!',
    'yes': 'Yes',
    'no': 'No',
    'left': 'Left side',
    'right': 'Right side',
    'centr': 'Both sides',
    'le372': 'Less than 37.2',
    'le385': 'Between 37.2 and 38.5',
    'mo385': 'More than 38.5'}

LEXICON_RU: Dict[str, str] = {
    '/help': 'просто напишите /start',
    '/abort': 'Вы прервали заполнение анкеты, до свидания!', 
    'begin': 'Давайте начнем!',
    'stop': 'Не сегодня!',
    'yes': 'Да',
    'no': 'Нет',   
    'left': 'Левая сторона',
    'right': 'Правая сторона',
    'centr': 'С обеих сторон',
    'le372': 'Меньше, чем 37.2',
    'le385': 'Между 37.2 и 38.5',
    'mo385': 'Больше, чем 38.5'}

LEXICON_FR: Dict[str, str] = {
    '/help': 'Imprimez /start',
    '/abort': 'Vous aves arrete votre mal-de-tete check pour aujoutd\'hui. Au revoir!',
    'begin': 'Allez y!',
    'stop': 'Prochaine fois!',
    'yes': 'Oui',
    'no': 'Non',
    'left': 'Cote gauche',
    'right': 'Cote droit',
    'centr': 'Deux cotes',
    'le372': 'Moins que 37.2',
    'le385': 'Entre 37.2 et 38.5',
    'mo385': 'Plus que 38.5'} 

BUTTONS: Dict[str, str] = {
    'btn0': '0',
    'btn1': '1',
    'btn2': '2',
    'btn3': '3',
    'btn4': '4',
    'btn5': '5',
    'btn6': '6'}

LEXICON: Dict[str, dict] = {'ru': LEXICON_RU, 'en': LEXICON_EN, 'fr': LEXICON_FR}