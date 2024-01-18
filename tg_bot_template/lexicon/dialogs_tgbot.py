from typing import Dict

# Initialize dictionary for DIALOG


# Dictionary for dialogs in rus
DIALOG_RU: Dict[str, str] ={
        'intro': 'Здравствуйте! Я - Headache-checker Bot. Каждый день я буду отправлять вам опрос,'
        ' который поможет оценить как часто у вас болит голова и что на это влияет.',
        'lvl': 'От 0 до 5, где 0 - это отсутствие симптомов, '
        'а 5 - непереносимая боль, оцените уровень вашей головной боли сегодня.',
        'localisation': 'Ок. Посмотрите на картинки и выберите номер от 1-6, соответстующий локализации вашей боли.',
        'lr': 'С какой стороны вы чувствуете боль?',
        'alcohol': 'Употребляли ли вы вчера алкоголь?',
        'pres_yn': 'Есть ли у вас возможность имерить артериальное давление?',
        'press_dat': 'Введите результаты измерения. \n\n'
                'Обратите внимания! Техника измерения очень сильно влияет на результат,\
                      рекомендуем ознакомиться с инструкцией!',
        'instr': 'Не ешьте и не пейте минимум в течение 30 минут перед процедурой\n'
            'Вам не должно хотеться в туалет\n'
            'Удобно расположитесь в кресле: спина должна поддерживаться, стопы на полу, \
                сидите прямо, не скрещивая конечности\n'
            'Рука для измерения должна находиться в расслабленном состоянии на уровне вашей груди.\n'
                'Убедитесь, что манжета надета на руку плотно, но не перетягивает руку.\n'
                'Манжета надевается на голую кожу, не поверх одежды.\n'
                'Не разговаривайте во время процедуры.\n\n'
                'Повторите процедуру три раза с интервалом в одну-две минуты.',
        'fever': 'Есть ли у вас повышенная температура?',
        'sleep': 'От 1 до 5 оцените как вы спали сегодня ночью, где 5 - \"Я спал как младенец!\",\
            а 1 - \"Я вообще не спал\"',
        'meteo': 'Нет никаких свидетельств о том, что солнечная/геомагнитная активность или атмосферное \
            давление как-то влияют на состояние человека. Тем не менее жара, или сильный холод однозначно могут влиять \
                на ваше самочувствия. Пожалуйста, разрешите мне определить ваше местоположение, \
                а я посмотрю какая у вас там погода',
        'met_true': 'Данная информация о погоде верна? ',
        'met_false': 'Пожалуйста, опишите сегодняшнюю погоду в формате: температура воздуха(в градусах Цельсия), \
            дождливо/солнечно, ветренно/спокойно, жарко/морозно',
        'add':'Здесь вы можете добавить любую дополнительную информацию о вашем состоянии, иначе \"-\"',
        'bye': 'Большое спасибо за Ваше время! Я сохраню вашу информацию и подготовлю статистический расчет! \
            Все предоставленные данные доступны только вам и не могут быть переданы третьим лицам.'
       
}

DIALOG_EN: Dict[str, str] ={
        'intro': 'Hello! This is the Headache-checker Bot. Everyday I will send you a survey that'
                 ' will help to estimate how often you have a headache and what affects it. ',
        'lvl': 'From 0 to 5, where 0 - is absence of headache symptomes '
               'and 5 is unsupportable pain, estimate the level of your headache today.',
        'localisation': 'Ok. What is localisation of your headache? Choose from 1 to 6 based on the picture',
        'lr': 'which side of the head is acking?',
        'alcohol': 'Did you drink alcohol yesterday?',
        'pres_yn': 'Can you measure your blood pressure now?',
        'press_dat': 'Please, entrer the results\n\n'
            'NB! Result may be strongly altered if your technique is uncorrect, you can look at the guide below',
        'instr': 'Before the procedure:\n\
            Don\'t eat or drink anything 30 minutes before you take your blood pressure\n\
                Empty your bladder \n\
                    Sit in a comfortable chair with your back supported, feet on the floor \
                        and no crossed limbs for at least 5 minutes\n\
                            Rest your arm with the cuff on a table at chest height.\n\
                                Make sure the blood pressure cuff is snug but not too tight.\
                                    The cuff should be against your bare skin, not over clothing.\
                                        Do not talk while your blood pressure is being measured.',
        'fever': 'Do you have a fever?',
        'sleep': 'From 1 to 5 estimate how did you sleep today, where 5 is \"I slept like a baby\" \
            and 1 is \"I didn\'t sleep\"',
        'meteo': 'There is no evidence that solar activity or athmospherical pressure \
            can affect your health state but heat or cold surely can. Please let me geolocalize your device\
                so I can look at the meteo and see if there are any correlation with your headache',
        'met_true': 'Is this information correct?',
        'met_false': 'Please write your meteo in the format: temperature deg C, rainy/sunny, windy/calm, feels hot/feels freezy',
        'add': 'Here you can add anything you want about general condions or some notes you consider important, otherwise \"-\"',
        'bye': 'Ok! Thank you for your time! I noted all information to prepare end-of-week statistics. \
            All provided data is for your personal use only and will be not trnsmitted to third parties.'
}

DIALOG_FR: Dict[str,str] = {
        'intro': 'Bonjour! Je suis le Headache-checker Bot. Chaque jour je vous enverrai un questionnaire, \
            qui vais aider à évaluer la frequance de vos maux de tête.',
        'lvl': 'De 0 à 5, évaluez le niveau de votre mal de tête aujourd\'hui, \
            0 - aucune douleur, 5 - douleur insupportable.',
        'localisation': 'D\'accord. Regardez les images et choisissez le numéro qui correspond à la localisation de votre douleur.',
        'lr': 'Quelle cote de tet est plus mal?',
        'alcohol': 'Est-ce que vous avez bu l\'alcool hier?',
        'pres_yn': 'Est ce que vous avez la moyenne de mesurer votre tension artérielle?',
        'press_dat': 'entrez le résultat.\n\n'
             'Attention! La technique de mesure influence beaucoup sur le résultat! Regardez l\'instruction en bas',
        'instr': 'Pendant les 30 minutes avant la mesure, ne faites pas d\'exercice physique, ne fumez pas, \
            évitez de manger et ne consommez pas de caféine.\n\
                Pour prendre votre tension artérielle, installez-vous dans une pièce calme, à température confortable. \
                    Asseyez-vous et restez assis pendant 3 à 5 minutes. \n\
                         Votre dos est soutenu par le dossier de la chaise. \
                            Vos jambes ne sont pas croisées et vos pieds sont posés à plat sur le sol. \
                                Placez votre bras nu sur une table. Le milieu du bras est au niveau du cœur. \
                                    Posez le brassard sur votre bras nu, en respectant le sens indiqué sur l\'appareil. \
                                        Réaliser 3 mesures espacées d\'une à deux minutes',
        'fever':'Est-ce que vous avez une fièvre ? ',
        'sleep': 'Entre 1 et 5, évaluez comment vous avez dormi, ou 5 - \"J\'ai dormi comme un bebe!\" et 1 - \"Je n\'ai pas du tout dormi.\"',
        'meteo': 'Il n\'y a aucune preuve que l\'activité solaire/géomagnétique ou la pression atmosphérique puisse affecter votre santé. \
            Par contre vous pouvez être sensible au chaleur ou au froid. Permettez-moi vous geolocaliser, je regardarai votre meteo.',
        'met_true': 'Est-ce que c\'est correct?',
        'met_false': 'Veuillez décrire la météo du jour au format: température de l\'air (en degrés Celsius),\
             pluvieux/ensoleillé, venteux/calme, chaud/gelé',
        'add': 'Ici vous pouvez ajouter tout l\'information additionel concernant votre etat ou \"-\".',
        'bye': 'Merci beaucoup pour votre temps! Je vais enregistrer vos informations et préparer un calcul statistique! \
             Toutes les données fournies ne sont disponibles que pour vous et ne peuvent pas être transférées à des tiers.'
}

# depending on language defined as global in user_handlers choose dictionary
DIALOG: Dict[str, dict] = {'ru': DIALOG_RU, 'en': DIALOG_EN, 'fr': DIALOG_FR}