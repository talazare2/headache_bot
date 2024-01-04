def dialog_message(lang):
    if lang == 'en':
        mes_1 = 'Hello! This is the Headache-checker Bot. Everyday I will send you a survey that \
            will help to estimate how often you have a headache and what affects it. '
        mes_2 = 'Let\'s start. From 0 to 10, where 0 - is absence of headache symptomes \
              and 10 is unsupportable pain, estimate the level of your headache today.'
        mes_3 = 'Ok. What is localization of your headache? Choose from 1 to 6 based on the picture'
        mes_4 = 'Did you drink alcohol yesterday? (answer: yes or no)'
        mes_5 = 'If you can measure your blood pressure enter results, otherwise \"-\"\n\
            NB! Result may be strongly altered if your technique is uncorrect\n\
                if you want short instruction write \"help\"'
        mes_help = 'Before the procedure:\n\
            Don\'t eat or drink anything 30 minutes before you take your blood pressure\n\
                Empty your bladder \n\
                    Sit in a comfortable chair with your back supported, feet on the floor \
                        and no crossed limbs for at least 5 minutes\n\
                            Rest your arm with the cuff on a table at chest height.\n\
                                Make sure the blood pressure cuff is snug but not too tight.\
                                    The cuff should be against your bare skin, not over clothing.\
                                        Do not talk while your blood pressure is being measured.'
        mes_6 = 'Do you have a fever? Enter result of measurement or \"-\"'
        mes_7 = 'From 1 to 5 estimate how did you sleep today, where 5 is \"I slept like a baby\" \
            and 1 is \"I didn\'t sleep\"'
        mes_8 = 'There is no evidence that solar activity or athmospherical pressure \
            can affect your health state but heat or cold surely can. Please write where are you now (city or zip-code)\
                so I can look at the meteo and see if there are any correlation with your headache'
        mes_9 = 'Is this information correct? (answer: yes or no)'
        mes_meteo = 'Please write your meteo in the format: temperature deg C, rainy/sunny, windy/calm, feels hot/feels freezy'
        mes_10 = 'Here you can add anything you want about general condions or some notes you consider important, otherwise \"-\"'
        mes_bye = 'Ok! Thank you for your time! I noted all information to prepare end-of-week statistics. \
            All provided data is for your personal use only and will be not trnsmitted to third parties.'
    elif lang == 'ru':
        mes_1 = 'Здравствуйте! Я - Headache-checker Bot. Каждый день я буду отправлять вам опрос, \
            который поможет оценить как часто у вас болит голова и что на это влияет. '
        mes_2 = 'Давайте начнем. От 0 до 10, где 0 - это отсутствие симптомов, \
              а 10 - непереносимая боль, оцените уровень вашей головной боли сегодня.'
        mes_3 = 'Ок. Посмотрите на картинки и выберите номер от 1-6, соответстующий локализации вашей боли.'
        mes_4 = 'Употребляли ли вы вчера алкоголь? (Варианты ответов: \"да\" или  \"нет\")'
        mes_5 = 'Если у вас есть возможность измерить ваше артериальное давление, введите\
            результаты измерения. Если нет - введитe \"-\"\n\
                Обратите внимания! Техника измерения очень сильно влияет на результат!\n\
                    Если вам нужна краткая инструкция, введите \"help\"'
        mes_help = 'Перед процедурой:\n\
            Не ешьте и не пейте минимум в течение 30 минут перед процедурой\n\
                Вам не должно хотеться в туалет\n\
                    Удобно расположитесь в кресле: спина должна поддерживаться, стопы на полу, \
                        сидите прямо, не скрещивая конечности\n\
                            Рука для измерения должна находиться в расслабленном состоянии на уровне вашей груди.\n\
                                Убедитесь, что манжета надета на руку плотно, но не перетягивает руку.\
                                    Манжета надевается на голую кожу, не поверх одежды.\
                                        Не разговаривайте во время процедуры.\n\
                                            Повторите процедуру три раза с интервалом в одну-две минуты.'
        mes_6 = 'Есть ли у вас повышенная температура? Введите результат измерения или \"-\"'
        mes_7 = 'От 1 до 5 оцените как вы спали сегодня ночью, где 5 - \"Я спал как младенец!\",\
            а 1 - \"Я вообще не спал\"'
        mes_8 = 'Нет никаких свидетельств о том, что солнечная/геомагнитная активность или атмосферное \
            давление как-то влияют на состояние человека. Тем не менее жара, или сильный холод однозначно могут влиять \
                на ваше самочувствия. Пожалуйста, напишите где вы находитесь (название города или почтовый индекс), \
                а я посмотрю какая у вас там погода'
        mes_9 = 'Данная информация о погоде верна? (Варианты ответов: \"да\" или  \"нет\")'
        mes_meteo = 'Пожалуйста, опишите сегодняшнюю погоду в формате: температура воздуха(в градусах Цельсия), \
            дождливо/солнечно, ветренно/спокойно, жарко/морозно'
        mes_10 = 'Здесь вы можете добавить любую дополнительную информацию о вашем состоянии, иначе \"-\"'
        mes_bye = 'Большое спасибо за Ваше время! Я сохраню вашу информацию и подготовлю статистический расчет! \
            Все предоставленные данные доступны только вам и не могут быть переданы третьим лицам.'
    elif lang == 'fr':
        mes_1 = 'Bonjour! Je suis le Headache-checker Bot. Chaque jour je vous enverrai un questionnaire, \
            qui vais aider à évaluer la frequance de vos maux de tête.'
        mes_2 = 'Commençons! De 0 à 10, évaluez le niveau de votre mal de tête aujourd\'hui, \
            0 - aucune douleur, 10 - douleur insupportable.'
        mes_3 = 'D\'accord. Regardez les images et choisissez le numéro (entre 1 et 6) qui correspond à la localisation de votre douleur.'
        mes_4 = 'Est-ce que vous avez bu l\'alcool hier? (Options de réponse : \"oui\" ou \"non\".)'
        mes_5 = 'Si vous avez la moyenne de mesurer votre tension artérielle, entrez le résultat. Sinon entrez \"-\"\n\
             Attention! La technique de mesure influence beaucoup sur le résultat!\n\
                 Si vous avez besoin d\'instruction entrez \"help\"'
        mes_help = 'Pendant les 30 minutes avant la mesure, ne faites pas d\'exercice physique, ne fumez pas, \
            évitez de manger et ne consommez pas de caféine.\n\
                Pour prendre votre tension artérielle, installez-vous dans une pièce calme, à température confortable. \
                    Asseyez-vous et restez assis pendant 3 à 5 minutes. \n\
                         Votre dos est soutenu par le dossier de la chaise. \
                            Vos jambes ne sont pas croisées et vos pieds sont posés à plat sur le sol. \
                                Placez votre bras nu sur une table. Le milieu du bras est au niveau du cœur. \
                                    Posez le brassard sur votre bras nu, en respectant le sens indiqué sur l\'appareil. \
                                        Réaliser 3 mesures espacées d\'une à deux minutes'
        mes_6 = 'Est-ce que vous avez une fièvre ? Entrez le résultat de mesure ou \"-\"'
        mes_7 = 'Entre 1 et 5, évaluez comment vous avez dormi, ou 5 - \"J\'ai dormi comme un bebe!\" et 1 - \"Je n\'ai pas du tout dormi.\"'
        mes_8 = 'Il n\'y a aucune preuve que l\'activité solaire/géomagnétique ou la pression atmosphérique puisse affecter votre santé. \
            Par contre vous pouvez être sensible au chaleur ou au froid. Entrez le nom de votre ville et/ou le code postale, je regardarai votre meteo.'
        mes_9 = 'Est-ce que c\'est correct?(Options de réponse : \"oui\" ou \"non\".)'
        mes_meteo = 'Veuillez décrire la météo du jour au format: température de l\'air (en degrés Celsius),\
             pluvieux/ensoleillé, venteux/calme, chaud/gelé'
        mes_10 = 'Ici vous pouvez ajouter tout l\'information additionel concernant votre etat ou \"-\".'
        mes_bye = 'Merci beaucoup pour votre temps! Je vais enregistrer vos informations et préparer un calcul statistique! \
             Toutes les données fournies ne sont disponibles que pour vous et ne peuvent pas être transférées à des tiers.'
    ans_tuple = (mes_1, mes_2, mes_3, mes_4, mes_5, mes_help, mes_6, mes_7, mes_8, mes_9, mes_meteo, mes_10, mes_bye)
    return ans_tuple

