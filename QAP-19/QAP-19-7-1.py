def customer_support_simulator(requests):
    replies = {1: {'req': 'ошибка', 'rep': 'Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.'}, 
               2: {'req': 'заказ', 'rep': 'Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.'}, 
               3: {'req': 'вернуть', 'rep': 'Вы можете вернуть товар в течение 14 дней с момента получения.'}, 
               4: {'req': None, 'rep': 'Благодарим вас за обращение. Ваш вопрос передан специалистам.'}}
    answers = []
    for req in requests:
       fold = req.casefold()
       if replies[1]['req'] in fold: answers.append(replies[1]['rep'])
       elif replies[2]['req'] in fold: answers.append(replies[2]['rep'])
       elif replies[3]['req'] in fold: answers.append(replies[3]['rep']) 
       else: answers.append(replies[4]['rep']) 
    return answers



questions = ["Это какая-то ошибка. Почему мой заказ еще не пришел? Я хочу вернуть средства."]
answers = customer_support_simulator(questions)
for i, answer in enumerate(answers):
   print(f'Question №{i + 1}: {questions[i]}')
   print(f'Answer: {answer}')

# Question №1: Это какая-то ошибка. Почему мой заказ еще не пришел? Я хочу вернуть средства.
# Answer: Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.

questions = ["Почему мой заказ еще не пришел?", "Возникла ошибка при оплате", "Как мне вернуть товар?"]
answers = customer_support_simulator(questions)
for i, answer in enumerate(answers):
   print(f'Question №{i + 1}: {questions[i]}')
   print(f'Answer: {answer}')
#  Question №1: Почему мой заказ еще не пришел?
# Answer: Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.
# Question №2: Возникла ошибка при оплате
# Answer: Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.
# Question №3: Как мне вернуть товар?
# Answer: Вы можете вернуть товар в течение 14 дней с момента получения.